import tensorflow as tf
from kerastuner.tuners import RandomSearch
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.datasets import fashion_mnist
from tensorflow.keras.callbacks import EarlyStopping, LearningRateScheduler


(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

train_images = train_images / 255.0
test_images = test_images / 255.0
def build_model(hp):
    model = keras.Sequential()
    model.add(layers.Flatten(input_shape=(28, 28)))
    for i in range(hp.Int('num_layers', 1, 3)):
        model.add(layers.Dense(units=hp.Int('units_' + str(i), min_value=32, max_value=512, step=32),
                               activation='relu'))

    model.add(layers.Dense(10, activation='softmax'))
    hp_learning_rate = hp.Choice('learning_rate', values=[1e-2, 1e-3, 1e-4])
    optimizer = keras.optimizers.Adam(learning_rate=hp_learning_rate)
    model.compile(optimizer=optimizer,
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])

    return model

early_stopping = EarlyStopping(monitor='val_loss', patience=5)

def scheduler(epoch, lr):
    if epoch < 10:
        return lr
    else:
        return lr * tf.math.exp(-0.1)

learning_rate_scheduler = LearningRateScheduler(scheduler)

tuner = RandomSearch(
    build_model,
    objective='val_accuracy',
    max_trials=5,
    executions_per_trial=1,
    directory='my_dir',
    project_name='fashion_mnist_tuning'
)

tuner.search(train_images, train_labels, epochs=50, validation_split=0.2,
             callbacks=[early_stopping, learning_rate_scheduler])

tuner.fit(train_images, train_labels, epochs=50, validation_split=0.2, callbacks=[early_stopping, learning_rate_scheduler])
test_loss, test_accuracy = tuner.evaluate(test_images, test_labels)

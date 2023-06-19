import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv1D, MaxPooling1D, Flatten, Dense, LSTM
import matplotlib.pyplot as plt

data = pd.read_csv('data.csv')
labels = pd.read_csv('data_labels.csv')
merged_data = pd.merge(data, labels, on='sequence')
merged_data = merged_data.sample(frac=0.2, random_state=42)

X = merged_data.iloc[:, 3:16].values
y = merged_data['state'].values
scaler = StandardScaler()
X = scaler.fit_transform(X)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
X_val, X_test, y_val, y_test = train_test_split(X_test, y_test, test_size=0.5, random_state=42)

X_train = X_train.reshape(X_train.shape[0], X_train.shape[1], 1)
X_val = X_val.reshape(X_val.shape[0], X_val.shape[1], 1)
X_test = X_test.reshape(X_test.shape[0], X_test.shape[1], 1)

cnn_model = Sequential()
cnn_model.add(Conv1D(32, 3, activation='relu', input_shape=(13, 1)))
cnn_model.add(MaxPooling1D(2))
cnn_model.add(Flatten())
cnn_model.add(Dense(64, activation='relu'))
cnn_model.add(Dense(1, activation='sigmoid'))
cnn_model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
cnn_history = cnn_model.fit(X_train, y_train, validation_data=(X_val, y_val), epochs=10, batch_size=32)
cnn_loss, cnn_accuracy = cnn_model.evaluate(X_test, y_test)

rnn_model = Sequential()
rnn_model.add(LSTM(64, input_shape=(13, 1)))
rnn_model.add(Dense(1, activation='sigmoid'))
rnn_model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
rnn_history = rnn_model.fit(X_train, y_train, validation_data=(X_val, y_val), epochs=10, batch_size=32)
rnn_loss, rnn_accuracy = rnn_model.evaluate(X_test, y_test)

print("CNN Accuracy:", cnn_accuracy)
print("RNN Accuracy:", rnn_accuracy)
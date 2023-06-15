import os
def join(start, end):
    text_files = []
    for k in range(start, end):
        if os.path.exists('clean_data/output' + str(k) + '.txt'):
            with open('clean_data/output' + str(k) + '.txt', 'r', encoding='utf-8') as f:
                text = f.read()
                text_files.append(text)
        
    joint_text = ''.join(text_files)

    with open('output.txt', 'w', encoding='utf-8') as f:
        f.write(joint_text)

    print("Joint text files from {}, {} to a file output.txt".format(start, end-1))

join(1, 300)
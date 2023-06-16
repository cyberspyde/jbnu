count = 0;  
import numpy as np
#Opens a file in read mode  
file = open("data.txt", "r", encoding="mbcs")  
word_list = []
whole_str = ""
#Gets each line till end of file is reached  
for line in file:  
    #Splits each line into words  
    words = line.split(" ");  
    #Counts each word  
    count = count + len(words);  
    word_list.append(words)

    lines = file.readlines()

string = str(lines).translate({ord("'"): None })
string = str(lines).translate({ord("["): None })
string = str(lines).translate({ord("]"): None })
string = str(lines).translate({ord("\\"): None })
string = str(lines).translate({ord("#"): None })

print(string)
counts = dict()

for word in s:
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1

file.close();  

print(counts)
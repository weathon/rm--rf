import os
import random
char_list=[".",";",":"]
for i in range(ord('a'),ord('a')+23):
    char_list.append(chr(i))
for i in range(ord('A'),ord('a')+23):
    char_list.append(chr(i))
for i in range(300):
    file_name=""
    for j in range(10):
        file_name+=random.choice(char_list)
    print(file_name+"   "+str(i)+"/300")
    #If yours is python2, here maight be print file_name,i,"/ 300"
    f=open(file_name,"w")
    f.close()
    

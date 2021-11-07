handle = open('E:\H T M L File\Python\file_handle\demo.txt')
sentencecount = 0 
for line in handle:
    word_count=0
    for char in line:
        if char == ' ':
             wordcount+=1
             if char ==' . ':
                    sentence_count+= 1
                    print(f'number of words in{sentence_count} = {word_count + 1}')

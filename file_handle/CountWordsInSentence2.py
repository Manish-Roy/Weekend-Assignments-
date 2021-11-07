def p (sentence_count , word_count):
    print(f'number of words in{sentence_count}={word_count+1}')
    handle = open('E:\H T M L File\Python\file_handle\demo.txt')


    sentence_count=0
    for line in handle:
        word_count=0
        for char in line:
            if char == ' ':
                word_count+=1
            elif char ==' . ' or char =='!' or char == '?':
                sentence_count+=1
                p(sentence_count. word_count)
                word_count= 0
                handle.writable()
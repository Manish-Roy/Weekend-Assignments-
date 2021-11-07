handle = open ('E:\H T M L File\Python\file_handle\demo.txt')
print (handle.read)
for line in handle:
    print(line, end = '')
    data = handle.readline()
    while data: 
        print(data , end='')
        data = handle.readline()
        
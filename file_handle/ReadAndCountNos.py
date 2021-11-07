def main():
 handle = open ('E:\H T M L File\Python\file_handle\demo.txt')
 print (handle.read())
 length = handle.tell()
 print(length + 1)
 handle.seek(0)
 print(line_chars(handle))




def line_chars(handle):
    return len(handle.readline())
    main()
filehandle = "E:\H T M L File\Python\file_handle\download.jpg"
handle = open( file, 'rb')
handle.close()

file ='E:\H T M L File\Python\file_handle\download.jpg'
handle = open(file,'wb')
handle.write(img)
handle.flush()
handle.close()
print('done')
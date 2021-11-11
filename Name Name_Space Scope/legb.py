name = 'MS Dhoni'            # global scope
def hometown():
    global name
    name = 'mahi'            # local scope 
    print (f'{name} , {id (name)}')


    hometown()
    print(f'{name} , {id (name)}')
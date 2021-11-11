name = 'MS Dhoni'               # global scope 
def hometown():
    global name
    name= 'Mahi'                # local scope 
    print(f'{name}  ,   {id (name)} ')   


def sis():
        #global name
        non-localname 
        name = 'bro' 
        

        print(f'{name} , {id(name)} inner ')


sis()
print (f'{name} , { id (name)} outer most')


homwtown()
print(f'{name} , { id (name)}  outermost')


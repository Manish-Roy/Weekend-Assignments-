class Circle:
    pi = 3.14
def __init__(self,r):
      self.r = r

def area(self):
    return self.pi*(self.r ** 2)

def vol(self):
    return self.pi*(self.r ** 3)


def cir(self):
    return 2 * self.pi * self.r 

def me(self):
        print(f' area of a circle is {self.area()}')
        print(f' volume of a circle is {self.circumference()}')
        print(f' circumference of a circle is {self.circumference()}')


r = float(input('Enter the radius : '))
obj = cir(r)
obj.me()
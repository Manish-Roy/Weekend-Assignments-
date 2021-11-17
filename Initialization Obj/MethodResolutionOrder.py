# Method Resolution Order


class Base1:
    var = 10
    class Base2:
        var = 100

class Derived( Base1, Base2):    # we can change class Derived (Base2 , Base1)
    def m1(self):
        print(f' from the Base1{self.var} ' )

    def m2(self):
        print(f' from the Base2{self.var} ' )


        0 = Derived()
        0.m1()
        0.m2()
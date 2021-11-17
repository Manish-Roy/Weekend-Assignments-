class Base:                      # Single Level Inheritance
    num = 100
    class derived(Base):
        
        
        def square(self):
            return self.num**2


        0 = derived()
        print(0,square())



    # Multi Level Inheritance
        class Base1:
             num = 10


    class semiBase(Base1):
        n=4


        class Derived(semiBase):


            def m1(self):
                print(f' from base class {self.num} ' )

            def m2(self):
                print(f' from semi Base class {self.n} ' )




            0 = Derived()
            0.m1()
            0.m2()   



        # Multiple Inheritance


class Base1:
    var = 10
    class Base2:
        var = 100

class Derived( Base2, Base1):    # After changing the values of Base1 to Base2 and viceversa class Derived (Base2 , Base1)
    def m1(self):
        print(f' from the Base1{self.var} ' )

    def m2(self):
        print(f' from the Base2{self.var} ' )


        0 = Derived()
        0.m1()
        0.m2()



        # Hierarchical Inheritance 


class square(Base):

    def square(self):
        print(f'{self.num**2}')


class cube(Base):
    def cube(self):
        print(f'{self.num**3}')

        object= square()
        object.square()
        object=cube()
        object.cube()
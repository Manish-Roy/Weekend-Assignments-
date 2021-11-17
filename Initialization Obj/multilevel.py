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
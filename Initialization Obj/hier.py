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
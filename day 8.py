# program 1
class calculator:
    # class level veriable
    c=10
    def __init__(self,x,y,z):
        # instance veriable
        self.x=x
        self.y=y
        self.z=z




tavish = calculator(1,2,3)
print(tavish.x)
print(tavish.y,tavish.z)
print(tavish.x + tavish.y +tavish.z)

print(tavish.c)
harshita=calculator(4,5,6)
print(harshita.c)


harshita.c=10000
print(harshita.c)
print(tavish.c)


# program 2
# changing values of instance level veriable

class calcu:
    a=10
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def changeX(self,change):
        self.x=change
    def changeY(self,change):
        self.y=change


tavisha=calcu(1,2)
print(tavisha.x)
harshitaa=calcu(2,3)
tavisha.changeX(78)
print(tavisha.x)
tavisha.changeY(67)
print(tavisha.y)


# program 3
class calci:
    d=4
    def __init__(self,x,y):
        self.x=x
        self.y=y

        @classmethod
        def changeD(cls,ch):
            cls.d=ch

tavishb=calci(4,5)
print(tavishb.d)



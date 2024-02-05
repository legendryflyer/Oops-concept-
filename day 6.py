# duck typing

class Human:
    def talk(self):
        print("hellow")

class Dog:
    def talk(self):
        print("bow bow")


def object_talk(object):
    object.talk()

c = Human()
d = Dog()

object_talk(c)


# oprator overloding
class Bookx:
    def __init__(self,pages):
        self.pages=pages

    def __add__(self, other):
        return self.pages + other.pages


class Bookz:
    def __init__(self,pages):
        self.pages=pages

ramayan=Bookx(200)
mahabharat=Bookz(150)

print(ramayan.pages+mahabharat.pages)
print(ramayan+mahabharat)

# method overloding

#class calculator:
#    def addition(self,x,y):
#        print(x+y)
#    def addition(self,x,y,z):
#        print(x,y,z)
#    def addition(self,x,y,z,a):
#        print(x+y+z+a)



class calculator:
    def addition(self,x=None,y=None,z=None,a=None):
        if x != None and y !=None and z !=None and a !=None:
            print(x+y+z+a)
        elif  x != None and y != None and z != None:
            print(x+y+z)
        elif x != None and y != None:
            print(x+y)

j=calculator()
j.addition(1,2,3,4)
j.addition(2,3)
j.addition(4,5,6)


# method overriding

class worldbank:
    def loan(self):
        print("i am from world bank")
    def save(self):
        print("i am save from world bank")

class SBI(worldbank):
    def loan(self):
        print("i am loan from SBI")
    def save(self):
        print("i am save from SBI")


nagpur = SBI()
nagpur.save()
nagpur.loan()








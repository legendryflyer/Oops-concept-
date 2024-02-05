# polymorphism
class duck:
    def talk(self):
        print("quack quack")

class human:
    def talk(self):
        print("hellow")
class dog:
    def talk(self):
        print("bow bow")

def call_talk(object):
    object.talk()

a=dog()
b=human()
c=duck()

call_talk(a)
call_talk(b)
call_talk(c)


# program 2
class Duck:
    def talk(self):
        print("quack quack")

class Human:
    def talk(self):
        print("hellow")
class Dog:
    def talk(self):
        print("bow bow")

class Cat:
    def sound(self):
        print("meow meow")

def call_talk_sound(object):
    if hasattr(object,'talk'):
        object.talk()
    elif hasattr(object,'sound'):
        object.sound()

x=Dog()
y=Human()
z=Duck()
w=Cat()
call_talk_sound(x)
call_talk_sound(y)
call_talk_sound(z)
call_talk_sound(w)



# oprator overlooding
print(1 +1)
print("1"+"1")  # string

class book:
    def __init__(self,x):
        self.pages =x
    def __add__(self, other):
        return self.pages + other.pages
class booky:
    def __init__(self,y):
        self.pages=y

ramayan=book(1000)
mahabharat=booky(500)

print(ramayan+mahabharat)



#program 4
class booka:
    def __init__(self,a):
        self.pages=a

class bookb:
    def __init__(self,y):
        self.pages=y
    def __gt__(self, other):
        return self.pages > other.pages

atomichabits=booka(1000)
geeta=bookb(400)

print(geeta > atomichabits)









# ducktyping

class duck:
    def talk(self):
        print("quack quack")
        
class human:
    def talk(self):
        print("hi hellow")
        
class cat:
    def mew(self):
        print("mewwww")
        

def callTalk(obj):
    if hasattr(obj, "talk"):
        obj.talk()
    else:
        obj.mew()
        
a=duck()
b=human()
c=cat()

callTalk(a)
callTalk(b)
callTalk(c)

# oprator overloding 

print("i"+"a") # string 
print(5+5) # integer 



class bookA:
    def __init__(self,pg):
        self.pages=pg
        
class bookB:
    def __init__(self,pg):
        self.pages=pg


    def __add__(self,other):
        return bookA(self.pages + other.pages)
    
    def __gt__(self,other):
        return bookA(self.pages > other.pages)

book1 = bookA(100)
book2 = bookB(80)
print(book1.pages + book2.pages)
print(book2.pages + book1.pages)

print(book1.pages>book2.pages)
print(book2.pages>book1.pages)


# overriding 

class Animal:
    def talk(self):
        print("I am an animal.")
        
class Cat(Animal):
    def talk(self):
        print("Meow!")
        
class Dog(Animal):
    def talk(self):
        print("Woof!")
        
        
d=Dog()
e=Cat()

d.talk()
e.talk()
        
        
    # overloding  of + operator for addition of objects of different classes
        
        
        
        
        

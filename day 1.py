class person:
    firstname =None
    lastname =None
    age =None
    rollno =None
    def displayName(self):
        print(self.firstname + self.lastname)

harshita = person()
print(harshita.firstname)
print(harshita.lastname)
print(harshita.age)
print(harshita.rollno)


harshita.firstname="tavish"
harshita.lastname="anade"
harshita.age="74"
harshita.rollno="68"
#print(harshita)
harshita.displayName()


#program 2
class persona:
    def __init__(self,fn,ln,ag,roll):
        self.firstName=fn
        self.lastName=ln
        self.age=ag
        self.rollno=roll


    def displayName(self):
        print(self.firstName + self.lastName)

tav= persona("tavish","anade","65","87")
print(tav)
 



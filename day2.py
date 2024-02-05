class student:
    def __init__(self,fn,ln,adhar):
        self.firstname = fn
        self.lastname=ln
        self.aadhar=adhar
    def displayName(self):
        return (self.firstname+self.lastname)

tavish=student("tavish","anade",64785898993576)
#print(tavish)
#print(tavish.firstname)
#print(tavish.lastname)
#print(tavish.aadhar)

class teacher(student):
    salary=10000000
    def displaysalary(self):
        return (self.salary)

tavish=teacher("tavish","anade",3276827360)
print(tavish.firstname)
print(tavish.lastname)
print(tavish.salary)
print(tavish.aadhar)
print(tavish.displayName())
print(tavish.displaysalary())



class harshita:
    def __init__(self,fn,ln,ag):
        firstname=fn
        lastname=ln
        age=ag

    def display(self):
        return (self.firstname + self.lastname)


class tavish(harshita):
    def __init__(self,fn,ln,ag,sn):
        super().__init__(fn,ln,ag)
        self.sname=sn

    def displaysname(self):
        return (self.sname)


tau=tavish("tavish","anade",376,"hg")
print(tau.displaysname())
print(tau.display())
print(tau.firstname)



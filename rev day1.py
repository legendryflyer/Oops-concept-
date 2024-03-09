#program 1
class Person:
    firstname = "tavish"
    lastname = "anade"
    age = 20
    roll = 10
    def display(self):
        return (self.firstname +" "+ self.lastname)
a = Person()
print(a.firstname)
print(a.lastname)
print(a.age)
print(a.roll)
print(a.display())

class personb:
    def __init__(self,fn,ln,ag,rn,sy):
        self.firstname = fn
        self.lastname = ln
        self.age = ag
        self.roll = rn
        self.salary = sy
    def displayName(self):
        return (self.firstname + " " + self.lastname)

    def displaySalary(self):
        return (self.salary)



b = personb("tavish","anade","20","30","0")
print(b.displayName())
print(b.displaySalary())

c=personb("ankit","bisikar","32","11","20")
print(c.displayName())
print(c.displaySalary())

d=personb("amit","bhisikar","35","138","26")
print(d.displayName())
print(d.displaySalary())


arr = [b,c,d]
for item in arr:
    print(item.displayName())
    print(item.displaySalary())









    
    

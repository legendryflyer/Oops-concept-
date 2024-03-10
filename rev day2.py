# class person:
#     def __init__(self,fn,ln,ag,rn):
#         self.firstname = fn
#         self.lastname = ln
#         self.age = ag
#         self.rank = rn
#     def displayName(self):
#         return (self.firstname +" "+self.lastname)
    
# tav = person("tavish","anade",20,1)
# print(tav.displayName())

class person:
    country="India" # class level veriable
    def __init__(self,fn,ln,ag,sl):
        self.firstname=fn
        self.lastname=ln
        self.age=ag
        self.salary=sl
       
    def showCountry(self):
        return self.country
    
    def displayName(self):
        return f"{self.firstname} {self.lastname}"
    
    def  displayAge(self):
        return self.age
    
    def showSalary(self):
        return self.salary
 
tav = person("tavish","anade",20,12345678900987654321)
print(tav.showCountry()) 
print(tav.displayName())
print(tav.displayAge())
tav.country = "bharat"
print(tav.showCountry()) 
print(tav.showSalary())


ankit = person("ankit","bhisikar",32,1234567890987654321)
print(ankit.displayName())
print(ankit.displayAge())
print(ankit.showCountry())
print(ankit.showSalary())



 

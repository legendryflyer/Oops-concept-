class student:
    def __init__(self,fn,ln,aadhar):
        self.firstname=fn
        self.lastname=ln
        self.aadhar=aadhar

    def display(self):
        return (self.firstname + "  "+self.lastname)



#tavish= student("tavish","anade","6348791")

#print(tavish.firstname)
#print(tavish.display())



class teacher(student):
    def __init__(self):
        super().__init__(fn,ln,aadhar,tn)
        self.name =tn

    def displayTn(self):
        return self.name






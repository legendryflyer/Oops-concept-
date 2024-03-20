class calci:
    def add(self,x,y):
        return(x+y)
    
    def add(self,x,y,z):
        return (x+y+z)
    
    def add(self,x,y,z,a):
        return (x+y+z+a)
    

h=calci()
print(h.add(1,2,3,4))


class calculator:
    def addition(self,x=None,y=None,z=None):
        if x != None and y !=None and z !=None : 
            return (x+y+z)
        elif x != None and y != None:
            return (x+y)


cccc=calculator()
print(cccc.addition(1,2))
print(cccc.addition(2,3,4))


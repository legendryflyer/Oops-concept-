# single inheritance 
class papa:
    def __init__(self,fn,ln):
        self.firstName = fn
        self.lastName = ln
        
    def display(self):
        print(self.firstName + " "+ self.lastName)


class beta(papa):  
    def __init__(self,fn,ln,bn):
        super().__init__(self,fn,ln)
        self.betaName = bn 
        
    def displayBetaName(self):
        print(self.betaName + " " + self.lastName) 
        
tavish =beta("tavish","anade","jr")
print(tavish.display())
print(tavish.displayBetaName())


# multi-level inheritance 

class father:
    def __init__(self,fn,ln):
        self.first_name = fn
        self.last_name = ln
        
    def displayName(self):
        return self.first_name

class son(father):
    def  __init__(self,fn,ln,sn):
        super().__init__(self,fn,ln)
        self.sonName = sn
        
    def displaySonName(self):
        return  self.sonName
    
class sonOfSon(son):
    def __init__(self,fn,ln,sn,ssn):
        super().__init__(self,fn,ln,sn)
        self.sonOfSonName = ssn
    
    def displayAllNames(self):
        return self.sonOfSonName


ankit = sonOfSon("tavish","anade","tavi","tav")
print(ankit.displayAllNames)  



    
        
    



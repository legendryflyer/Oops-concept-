class A(object):
    def add(self):
        print("A class method")
        super().add()
        
class B(object):
    def add(self):
        print("B class method")
        super().add()
        
class C(object):
    def add(self):
        print("c clas method")

class X(A,B):
    def add(self):
        print("X class method") 
        super().add()

class Y(B,C):
    def add(self):
        print("Y class method") 
        super().add()

class P(X,Y,C):
    def add(self):
        print("P class method") 
        super().add() 
        
p = P()
p.add()


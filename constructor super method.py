class Mi:
    def __init__(self,v):
        self.money=v
        print("mi team contructor")
    def show(self):
        print("mi team instance method",self.money)  

class Gt(Mi):
    def __init__(self,v,m):
        super().__init__(v)              #calling Mi class constructor
        self.player=m
        print("Gt team contructor")
    def disp(self):
        print("Gt team instance method:",self.money,"Player:",self.player)  

s=Gt(100000,12)  
s.disp()      
s.show()
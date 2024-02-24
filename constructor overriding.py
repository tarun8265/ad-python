class Mi:
    def __init__(self):
        self.money=10000000
        print("mi team contructor")
    def show(self):
        print("mi team instance method",self.money)  

class Gt(Mi):
    def __init__(self,v):
        self.money=v
        print("Gt team contructor")
    def disp(self):
        print("Gt team instance method")  

g=Gt(100000)
print(g.money)   
g.show()    
g.disp()   

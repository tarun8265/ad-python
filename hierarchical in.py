class Father:
    def __init__(self,m): 
        self.money=m
        print("Father class constructor")
    def show(self):
        print("Father class Method")

class Son(Father):
    def __init__(self,m):
        super().__init__(m)                    # calling father class constructor
        print("Son class constructor")
    def shows(self):
        print("Son class Method")

class Daughter(Father):
    def __init__(self):
        super().__init__()                   # calling father class constructor
        print("Daughter class constructor")
    def showd(self):
        print("Daughter class Method")    

s=Son(10)
print(s.money)

             
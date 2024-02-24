class Father:
    def __init__(self): 
        super().__init__()  
        print("Father class constructor")
    def show(self):
        print("Father class Method")

class Mother:
    def __init__(self):
        super().__init__()                   # calling father class constructor
        print("Mother class constructor")
    def shows(self):
        print("Mother class Method")

class Daughter(Father,Mother):
    def __init__(self):
        super().__init__()                   # calling father class constructor
        print("Daughter class constructor")
    def showd(self):
        print("Daughter class Method")    

d=Daughter()
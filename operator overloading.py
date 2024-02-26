# operator ovreloading

# print(10+20)

# print(str.__add__('hello','tarun'))

class A:
    def __init__(self,x):
        self.x=x
    def __add__(self,other):
        return self.x+other.x  

class B:
    def __init__(self,x):
        self.x=x
    

a=A(18)
b=B(18)
print(a+b)                 
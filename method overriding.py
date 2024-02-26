# class Add:
#     def result(self,a,b):
#         print("Addition:",a+b)

# class Multi(Add):
#     def result(self,x,y):
#         # super().result(12,12)
#         super().result(12,34)
#         print("MUlti:",x*y)

# n=Multi()
# n.result(12,34)        
        

class Add:
    def result(self,a,b):
        print("Addition:",a+b)

class Multi(Add):
    def result(self,x,y):
        print("MUlti:",x*y)

n=Multi()
n.result(12,34)  

m=Add()
m.result(10,20)
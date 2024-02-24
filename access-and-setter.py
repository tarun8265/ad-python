#instance method - accessor/getter method
# class Mobile:
#     def __init__(self):
#         self.mobile="pocom4"
#     def get_mobile(self):
#         return self.mobile

# poco=Mobile()
# n=poco.get_mobile()            
# print(n)


#instance method - mutator/setter method
# class Mobile:
#     def __init__(self):
#         self.mobile="poco m4"
#     def set_mobile(self):
#         self.mobile="poco m45g"  

# poco=Mobile()          
# print(poco.mobile)
# print()
# poco.set_mobile()
# print(poco.mobile)

#with parameter
class Mobile:
    def set_mobile(self,m):
        self.mobil=m

poco=Mobile()   
poco.set_mobile("poco m4")
print(poco.mobile)     


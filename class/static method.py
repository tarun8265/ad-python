# class Mobile:
#     # a=10
#     @staticmethod
#     def show_model():
#         print("poco")
#         # print(Mobile.a)

# poco=Mobile()     
# Mobile.show_model()   



#with parameter
class Mobile:

    @staticmethod
    def show_model(m,p):
        model=m
        price=p
        print("Model:",m,"Price:",p)
poco=Mobile()     
Mobile.show_model("poco",12000) 
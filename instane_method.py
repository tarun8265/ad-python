#instane method without parameter
class Mobile:
    def show_mobile(self):
        print("realme s2")
x=Mobile()
x.show_mobile()        


#instane method with parameter
class Mobile:
    def __init__(self):
        self.mobile="RealmeX"

    def show_mobile(self,p):
        price=p
        print(self.mobile,"and",price)
x=Mobile()
x.show_mobile(12000) 

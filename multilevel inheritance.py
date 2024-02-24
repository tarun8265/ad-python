class Father:
    def __init__(self):
        print("Father class contructor")
    def show(self):
        print("Father class instance method")  

class Son(Father):
    def __init__(self):
        super().__init__()
        print("Son class contructor")
    def disp(self):
        print("Son class instance method") 

class Grandson(Son):
    def __init__(self):
        super().__init__()
        print("Grandson class contructor")
    def dispg(self):
        print("Grandson class instance method")         

g=Grandson()       
g.show()
g.disp()
g.dispg()


# class Father:
#     def show(self):
#         print("Father class instance method")  

# class Son(Father):
#     def shows(self):
#         print("Son class instance method") 

# class Grandson(Son):
#     def showg(self):
#         print("Grandsoc class instance method")         

# g=Grandson()
# g.show()
# g.shows()
# g.showg()
         


#class method w/o parameter
# class Name:
#     # a="pari"
#     @classmethod
#     def show_name(cls):
#         print("tarun")
# n=Name()
# Name.show_name()       


#class method with parameter

class Name:
    a="rahul"
    @classmethod
    def show_name(cls,n):
        cls.second=n
        print(cls.a,"and",cls.second)

x=Name()
Name.show_name("tarun")

       

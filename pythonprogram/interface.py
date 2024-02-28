# from abc import ABC,abstractmethod
# class Force(ABC):
#     @abstractmethod
#     def gun(self):
#         pass
#     def area(self):
#         pass

# class Army(Force):
#     def gun(self):
#         print("Gun = AK47" )    
#     def area(self):
#         print("Army Area = Land") 

# class Airforce(Force):
#     def gun(self):
#         print("Gun = AK43" )    
#     def area(self):
#         print("Airforce Area = Sky") 

# class Navy(Force):
#     def gun(self):
#         print("Gun = AK46" )    
#     def area(self):
#         print("Navy Area = Sea") 


# a=Army()
# a.gun()
# a.area()             
# print()
# a=Airforce()
# a.gun()
# a.area()  
# print()
# a=Navy()
# a.gun()
# a.area()  



from abc import ABC,abstractmethod
class Father(ABC):
    @abstractmethod
    def disp1(self):
        pass
    @abstractmethod
    def disp2(self):
        pass
class Child(Father):
    def disp1(self):
        print("Child Class")
        print("dsp1 abstract class")
class Grandchild(Child):
    def disp2(self):
        print("Grandchild Class")
        print("disp2 abstract class")         
g=Grandchild()
g.disp1()
g.disp2()

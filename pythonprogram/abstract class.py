from abc import ABC , abstractmethod
class Father(ABC):
    @abstractmethod
    def disp(self):                                      # abstract method
        pass
    def show(self):
        print("concert method")                          # concert method or normal method

class Child(Father):
    def disp(self):
        print("child method")                            # abstract method calling
        print("Define Abstract Method")        

c=Child()
c.disp()
c.show()        
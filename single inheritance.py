class Mobile:
    a=10
    def show(self):
        print("Mobile is a best ")
    @classmethod
    def show_a(cls):
        print("Mobile no.",cls.a)   
    @staticmethod
    def stat():
        print("this is static method")

class Mobile2(Mobile):
    def disp(self):
        print("Mobile2 is a best")

n=Mobile2()
n.disp()
n.show()
n.show_a()
n.stat()
print()
m=Mobile()
m.show()
m.show_a()


class Mobile:
    a = 10                             #class variable

    def __init__(self):                #constructor
        self.mobile='Poco m4'          #instance variable

    def show_mobile(self):             #instance method
        print(self.mobile)
        
    @classmethod                       #class method
    def is_a(cls):
        print(cls.a)

poco=Mobile()
poco.show_mobile()
print(Mobile.a)
Mobile.is_a()
class Army:
    def __init__(self):
        self.name="rahul"
    def show(self):
        print("Name:",self.name)

    class Gun:
        def __init__(self):
            self.gun="AK47"    
            self.capacity="75 round"
            self.size="24 in"

        def disp(self):
            print("Gun:",self.gun)    
            print("Capacity:",self.capacity) 
            print("Size:",self.size) 
a=Army()            
print(a.name)
a.show()

g=Army().Gun()
g.disp()
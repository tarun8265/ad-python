# strong typing
class Duck:
    def walk(self):
        print("this is a duck")

class Horse():
    def walk(self):
        print("this is a horse")

class Cat:
    def talk(self):
        print("this is a cat")

def function(a):
    if hasattr(a,"walk"):
         a.walk()
    if hasattr(a,'talk'):
        a.talk()  

d=Duck()
function(d)

h=Horse()
function(h)

c=Cat()
function(c)
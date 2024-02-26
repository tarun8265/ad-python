class Myclass:
    def sum(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            s=a+b+c
        elif a!=None and b!=None:
            s=a*b
          
        else:
            s="minium provide two number:"  
        return s 

n=Myclass()
print(n.sum(19))        
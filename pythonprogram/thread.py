from threading import Thread
# def disp():
    # print("Thread Running")
def disp(a,b):
      print("Thread Running:",a, b)   
for i in range(5):
    t=Thread(target=disp,args=(10,20))

    t.start() 
    
       
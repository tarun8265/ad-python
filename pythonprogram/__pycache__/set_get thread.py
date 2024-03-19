from threading import Thread, current_thread
# def disp():
#     print("Current threading:",current_thread().getName())
# t=Thread(target=disp)    
# t.start()

# print("Main Threading:",current_thread().getName())



#     print("Current threading:",current_thread().getName())
#     current_thread().setName("child thread")
#     print("child threading:",current_thread().getName())
# t=Thread(target=disp)    
# t.start()

# print("Main Threading:",current_thread().getName())
# current_thread().setName("tarun thread")
# print("tarun threading:",current_thread().getName())

#     print("Current threading:",current_thread().name)
#     current_thread().name='child thread'
#     print("child threading:",current_thread().name)
# t=Thread(target=disp)    
# t.start()

# print("Main Threading:",current_thread().name)
# current_thread().name='tarun thread'
# print("tarun threading:",current_thread().name)

def disp():
    pass
# t=Thread(target=disp)
# print("Deafult:",t.getName())
# t.setName("child")
# print(t.setName)

# t=Thread(target=disp)
# print("Deafult:",t.name)
# t.name="child"
# print(t.name)

t=Thread(target=disp,name="raj")
print(t.name)
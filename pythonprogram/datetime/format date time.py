from datetime import datetime
dt=datetime.today()
print(dt)
print()

dt1=dt.strftime("%B%d,%Y")
print(dt1)
print(type(dt1))
print()

dt2=dt.strftime("%d/%b/%Y")
print(dt2)
print() 

dt3=dt.strftime("%H:%M:%S")
print(dt3)
print() 

dt4=dt.strftime("%I:%M:%S")
print(dt4)
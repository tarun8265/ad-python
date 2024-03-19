from datetime import date
dob=date(2007,9,9)
t=date.today()
age=t.year-dob.year-((t.month,t.day)<(dob.month,dob.day))
print(age)

print(2-False)
print(2-True)
import datetime as dt    #here we import the datetime package for using and we use a alias name dt for computation 

current_date=dt.date.today()    # it provides the current date 
print(current_date)  

new_date=dt.date(2024,3,26)  
print(new_date)
print(new_date.year)
print(new_date.month)
print(new_date.day)


print("-----------------------------------------------------------------")

current_time=dt.datetime.now()
print(current_time)

time=dt.time(8,12,10,53535)
print(time)
print(time.hour)
print(time.minute)
print(time.microsecond)


#creating a own datetime

datetime=dt.datetime(2024,3,24,9,23,56)
print(datetime)
print(datetime.date())
print(datetime.time())


current_date=dt.datetime.now()
my_birthdate=dt.datetime(2024,4,17)     # differnce of two dates 
difference=my_birthdate-current_date
print(difference)
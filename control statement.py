# if statement

number=int(input("enter the number:"))
if number%2 == 0:
    print(number,"is even ")
    
    
#if else statement 

name=input("enter your name : ")
marks=int(input("enter your mark : "))
if(marks>=80 and marks<=100):
    print("wow you got A  grade")
else:
    print("you got good grade")
    
#elif statement 
marks=int(input("enter your mark : "))
if(marks>=90 and marks<=100):
    print("wow you got A  grade")
elif(marks>=80 and marks<90):
    print("you got b grade ")
elif(marks>=70 and marks<80):
    print("you got b grade ")
else:
    print("you got failed")


# nested if statement 
num=int(input("enter the number : "))
if(num != 0):
    if(num%2 == 0):
         print(num,"is even ")
    
    
        
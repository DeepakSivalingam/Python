#looping statements
# for 
# while 


#printing the even number 
i=2
while i<=10:
    print(i)
    i+=2
    
#printing the odd numbers 
i=1
while i<10:
    print(i)
    i+=2

#range in python 

a=list(range(2,5)) # range(n,n-1)
print(a)

a=list(range(0,30,2))
b=list(range(1,30,2))
print(a)
print(b)

#for loop 
for i in range(5):
    print(i)

for i in range(3):
    x=int(input("enter the number : "))
    y=int(input("enter the number : "))
    print(x+y)
    

# nested for loops 

for i in range(6):
    for j in range(i):
        print("*",end="")
        
    print("")
    
print("------------------------------------------------------------------")


for i in range(5,0,-1):
    for j in range(i):
        print("*",end="")
    print("")
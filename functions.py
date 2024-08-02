# functions in python 
# function is block of code that  can  perform a specific task and it can be executed when it is called ..

name="deepak"
def function():
    print("welcome !"+name )

function()

 # 9 types of function
 
 #no return type and without arguments  function 
 
def add():
     a=int(input("enter the value of a : ")) 
     b=int(input("enter the value of b  : "))
     c=a+b
     print(c)
     
add()


#no return type with arguments

def add(a,b):
     c=a+b
     print(c)
     
add(23,54)

#return type without arguments

def add():
     a=int(input("enter the value of a : ")) 
     b=int(input("enter the value of b  : "))
     c=a+b
     return c
     
print("total",add())

#return type with arguements 
def add(a,b):
     c=a+b
     return c
     
print("total",add(45,65))

#arbitrary arguements  function -- we can pass several arguments 

def student(*details):
    print(details)
    for i in details:
        print(i)
    
student("deepak",20,"male")


#keyword arguements fuction 
def add(a,b):
     c=a+b            # this function resolves the problem of confusion of arguments values
     print(c)
     
add(b=45,a=65)


# arbitrary keyword arguements function 

def student(**detail):
    print(detail)
    
student(name="deepak",age=20,gender='male')


#default parameter arguements function 

def function(name,place="villupuram"):
    print(name ,"is living in ",place)

function("deepak")
function("sam","gingee")     # here the gingee overides the default parameter value villupuram


#passing a list as an arguement in function 

def total(marks):
    return sum(marks)

print("total :",total([98,89,90,92,91]))


#Recursion function -- a function call by itself 

def factorial(x):
    if x==1:
        return 1
    else:
        return (x*factorial(x-1))
    
print("factorial is : ",factorial(5))


#lamda function -- its a anonoyms function and without a function name...  used for simple calculations

x=lambda a : a*100
print(x(10)) 


x=lambda length,breadth: length*breadth
print(x(10,6)) 

n= lambda name: print('deepak')
n("s")


#example

def examp(a=int(input("enter the number of A ")),b=int(input("enter the number of B"))):
    return a+b,a-b,a*b
print(examp())




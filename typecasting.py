#type casting in python 

a=39.3
print(type(a))  # here we converting the float type to integer 
b=int(a)
print(b)
print(type(b))

c=3
d=float(c)     #here we converting the integer to float
print(type(d))


    # constructors used in python for typecasting 
    # int()
    #float()
    #str()
    
    
    #  , is used for placing the integer with the string value 
    
    
x=29
y=3
c=x+y
c="hi"
print("total :",c)

x=29
y=3
c=x+y
print("total : " +  str(c))


# note 

# string with numbers values can convert into int , float
# integer can convert into float , string
# float can convert into string ,integer

# string converted into integer
value ='35'
values = int(value)
print(type(values))

# string converted into float
value1 ='35'
values1 = float(value1)
print(type(values1))


example="hii"           # here we cant change the actual string  values into integer ,float 
example1=int(example)
print(type(example1))
#operators in python 
# PEMDEM

# arithmetic operator 
a=10
b=8
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a//b)
print(a**b)

#assignment operator 
#arithmetic assignment operator 
a=10
a+=5
print(a)
a-=5
print(a)
a*=5
print(a)
a/=5
print(a)
a%=5
print(a)
a//=5
print(a)
a**=5
print(a)


#comparison operator 
a=20
b=10
print(a==b)
print(a!=b)
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)


#logical operator 
# and
# or
#not
a=35
b=23
print(a>=30 and b<30)
print(a>=30 or b>30)
print(not(a>=30 and b>30))


# bitwise operator 

""""
 & and
 | or
 ^ xor
 ~ not
 << zero fil left shift 
 >> right shift 
"""

a=23
b=13
print(a&b)
print(a|b)
print(a^b)
print(~a)
print(a<<2)
print(a>>2)


#identity operator
# is 
# is not 

a=12
b=12
if a is b:
    print("same ")
else:
    print("different ")



if a is not b:
    print("different")
else:
    print("same ")

#membership operators

example="string "
print('s' in example)

list=[2,0.5,'helo']
print(5 in list)
print(5 not  in list)

#immutable 
# sorounded by the parenthesis .its similiar to list 



tuple=(2,'welcome',0.6)
print(tuple)
print(type(tuple))

# accesing the values and slicing 

print(tuple[2])
print(tuple[:])
print(tuple[-1])
tuple1=list(tuple)  # if there is any condition to change the value in tuple then we change the tuple  to list for achieving our target  
print(tuple1)
tuple1[1]="hiiiiiiiii"
print(tuple1)
tuple1.append("welcome")
print(tuple1)

'''c=tuple(tuple1) # here we changing the list to tuple
print(type(c))'''

#tuple functions 

example=(1,3,'python',0.3)
print(example)
print(len(example))
del example          # to delete the tuple 



example=(1,3,'python',0.3)
x=(2,3)                      # concatenation of two tuple
y=example+x
print(y)  

x=(2,3,2,2,6)  
print(x.count(2))


#nested tuple 
x=(2,3)  
y=(1,3,4.3,'hii')
tuple=(x,y)
print(tuple)
print(tuple[0][0])
print(tuple[1][3])
                
x=(2,3)*3      #repetition of values 
print(x)

x=(2,3)        # minimum and maximum values in the list .
print(max(x))
print(min(x))
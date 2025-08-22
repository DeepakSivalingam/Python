'''

  try
  except
  else
  finally

'''

try:
    a=10/0
except Exception as e:
    print(e)



try:
    a=10/1
except Exception as e:
    print(e)
else:                # else block is only  excuted when there is no exception 
    print(a)
finally:
    print("program ended!")
    
try:
    a=[1,0.4,'hii']
    print(a[3])
except Exception as e:
    print(e)
    
    
    #types of exceptions in python 
    
    print(dir(locals()['__builtins__']))
    print(len(dir(locals()['__builtins__'])))
    
    #name error exception 
    try:
        print(b)
    except NameError :
        print("b is not defined ")
        
        
    #file not found error 
    
    try:
        f=open("sample.py")
    except FileNotFoundError as e:
        print("FileNotFoundError")
    else:
        print(f.read())
        


# ARRAYS ---------------------------------------------

import array
arr=array.array('i',[5,3,9,1,6])
print(len(arr))

arr.append(2)
arr.insert(2,8484)

arr.pop([4])
arr.remove(3)

arr.extend([8789,242,42444])

arr3=[]
print(arr3.fromlist([323,45454,555])

print(arr.tolist())

arr.index(1)

arr.reverse()

arr.count(555)



 
    
    
    

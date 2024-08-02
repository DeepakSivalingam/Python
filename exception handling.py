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
        

 
    
    
    
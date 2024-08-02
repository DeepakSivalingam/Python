'''
class--it is a blue print or a templated for creating a individual objects ..methods and attributes
object-- instances of class..consist of methods and property 
object or instances
'''

'''
# class atributes 

class user_details:
    name="deepak"       # here we creted the class ...these are the class attributes 
    password="deepak2332"

# two ways to accesing the class attributes 

# one way-- getattr() method 

print(getattr(user_details,'name')) 
print(getattr(user_details,'password')) 
print(getattr(user_details,'gender','this attribute not found')) # the third parameter that specifies the exception that we given 

# dot notation 

print(user_details.name)
print(user_details.password)


# setattr -- for creating and changing the attibute 

setattr(user_details,'name','ram')
setattr(user_details,'gender','male')

user_details.city="villupuram"     # another way to create the attribute 
print(user_details.city)

print(getattr(user_details,'name'))
print(getattr(user_details,'gender'))


#delattr--- for deleting the attribute 

delattr(user_details,'gender')
print(user_details.__dict__)



# instance  atributes 

class student:
    department="IT"

object=student()    # here we created object for the above class

print(object.__dict__)

print(object.department)
object.department="CSE"
print(object.department)

# when we change or update the attributes by using the instance attribute it can't reflect in the class attributes .



#class methods

#example

class user_details:
    name="deepak"       
    password="deepak2332"
    
    def call():
        print("name :" ,user_details.name)
        print("password :" ,user_details.password)
        
user_details.call()


#instance methods 

class user_details:
    name="deepak"       
    password="deepak2332"
    
    def call(self):   # here the self is the instance methods 
        print("name :" ,user_details.name)
        print("password :" ,user_details.password)
        
object=user_details()
object.call()


#  here we passing a arguements 

class user_details:
    name="deepak"       
    password="deepak2332"
    
    def call(self,gender):   # here the self is the instance methods 0t 
        print("name :" ,user_details.name)
        print("password :" ,user_details.password)
        print("gender: ",gender)
        
object=user_details()
object.call("male")


# __init__   function--constructor method
# inbuilt function .. this function can be called when the object is created 
# it is used for runtime initialaization for the instance variables 

class init_function:
    def __init__(self,name):
        print("hiiii")
        self.name= name   #instance variable or object variable  
        
    def call(self):
        print("name : ",self.name)
        
o=init_function('deepak')
o.call()

o1=init_function('ram')
o1.call()

print(o.name)
print(o1.name)


#instance variable can be accesed by the object name 
#class varibale can be accesed by the class name 


'''



#  oop basics 

class User:

    def __init__(self,user_name,password):
          self.user_name= user_name          # here we putting the none for initialization because  here we creating a blueprint not for a particular person .
          self.password= password           #  we can provide  a any valid data like float,integer,tuple,dictionary 
                                            # instance variable .related to object
    
    def register(self):
        print("Registering......."+ self.user_name)
        
    def login(self):
        print("logging........")
    
user1=User("deepak","deepak2099")
user2=User("ram","ram2098")
user1.register()

print(user1.user_name)         # here we accesing the username
print(user2.user_name)    




class User:
    users=0       # class variable and it is common for all objects ......class variable can be accessed by class name 

    def __init__(self,user_name,password):
          self.user_name= user_name         #instance variable 
          self.password= password    
          User.users+=1       
                                           
    
    def register(self):
        print("Registering......."+ self.user_name)
        
    def login(self):
        print("logging........")
    
user1=User("deepak","deepak2099")
user2=User("ram","ram2098")
user1.register()
print(User.users)    # here we accessing the class variable 
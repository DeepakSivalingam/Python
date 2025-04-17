# method overriding

class user:      
    def register(self):
        print("registering ..........")
        
    def login(self):
        print("logging in ..............")
    
    def greet(self):
        print('hello!! welcomes you ')
        
class student(user):  
    def greet(self):
        print("welcome students")
        
class teacher(user):  
    def greet(self):
        print("welcome Teacher")
        
        
o=user()
o.greet()

o1=student()
o1.greet()

o2=teacher()
o2.greet()



# Duck Typing (Another Form of Polymorphism)
class Bird:
    def fly(self):
        print("Bird is flying.")

class Airplane:
    def fly(self):
        print("Airplane is flying.")

def takeoff(obj):
    obj.fly()  # As long as 'fly()' is defined, it works!

takeoff(Bird())       # ✅ Bird is flying
takeoff(Airplane())   # ✅ Airplane is flying






#method chaining


class user:      
    def register(self):
        print("registering ..........")
        
    def login(self):
        print("logging in ..............")
        return self
    
    def greet(self):
        print('hello!! welcomes you ')
        return self
 
o=user()
o.greet().login().register()     # here we gives the several methods in a single line 

                                 #here we want acces those methods in a single line thats why we give the return self ..

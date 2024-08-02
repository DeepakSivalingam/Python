''' super function is used to extract or access
    the methods or initialized variable from the parent class to their child class...
    
This super function is only applicable when we are using the inheritance concept .

Maximum try to avoid the multiple inheritance beacuse it makes confusion ...if you used then it will 
access the methods in a order way.....
 
'''

class User:
    count=1
    def __init__(self,username,password):
        self.username=username
        self.password=password
        
    def register(self):
        print("registered ",self.username)
        
class Student(User):
    
    def __init__(self,username,password,dept,fee):
        super().__init__(username,password)
        self.dept=dept
        self.fee=fee
        
    def login(self):
        super().register()
        print("logging in ")
        print(super().count)
        
        
student1=Student("deepak","deepak3233","IT",3287884)
print(student1.username)
print(student1.fee)
student1.login()
    
        

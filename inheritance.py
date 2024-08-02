#inhertance 
#technique for avoiding the redundancy 

class user:       #parent class or super class or base class
    def register(self):
        print("registering ..........")
        
    def login(self):
        print("logging in ..............")
        
class student(user):   # here the student class inherits the user class --child class or derived class or sub class
    def student_greeting(self):
        print("welcome students")
        
class teacher(user):   # here the teacher class inherits the user class --child class
    def teacher_greeting(self):
        print("welcome Teacher")


student1=student()
student1.student_greeting()
student1.login()
student1.register()

faculty1=teacher()
faculty1.teacher_greeting()
faculty1.login()
faculty1.register()

# we cannot access the child class methods from the parent class

# here we creating another class that inherit the techer class----this multi level inheritance 

class faculty(teacher):
    def trainee(self):
        print("hii traineee")
        
o=faculty()
o.trainee()
o.teacher_greeting()
o.login()
o.register


# multiple level inheritance 

class studentFaculty(student,teacher):
    def multiple(self):
        pass
o=studentFaculty()
o.login()
o.register()               # in the multiple inheritance we can acces the vaiables and methods of the parent and its grand parent of the class 
o.multiple()
o.student_greeting()
o.teacher_greeting()
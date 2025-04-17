# abstract classs

from abc import ABC,abstractmethod
#you can't create object for the abstract class
#classes inheriting the abstract class must implement the methods of the abstract classes unless the classes also consider as a abstract class

class vechicle(ABC):   #abstract class
    @abstractmethod   #decorator
    def start(self):
        pass
    
class bus(vechicle):       #concrete class
    def start(self):
        print("your bus  has been started")
    
class car(vechicle):       #concrete class
    def start(self):
        print("your car has been started")
            
            
object1=bus()
object1.start()





#naming conventions

'''
     single underscore before any methods or variable in a class then it is considered as a PROTECTED
     double underscore before any methods or variable in a class then it is considered as a PRIVATE 
     double underscore before and after the methods -- they are the PYTHON INTERNAL METHODS
       eg----  __main__,__name__
'''


# Encapsulation 
class Account:
    def __init__(self, balance):
        self.__balance = balance  # private variable

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

acc = Account(1000)
acc.deposit(500)
print(acc.get_balance())  # ✅ 1500
# print(acc.__balance) ❌ This will give an error (private)


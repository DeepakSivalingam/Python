# abstract classs

from abc import ABC,abstractmethod
#you can't create object for the abstract class
#classes inheriting the abstract class must implement the methods of the abstract classes unless the classes also consider as a abstract class

class vechicle(ABC):   #abstract class
    @abstractmethod   #decorator
    def start(self):
        pass
    
class bus(vechicle):
    def start(self):
        print("your bus  has been started")
    
class car(vechicle):
    def start(self):
        print("your car has been started")
            
            
object1=bus()
object1.start()



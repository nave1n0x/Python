#here in this progrma we are going to discus about yur abstract class is a class which used to make a class abstract nothing but if you want to initiate that particular class or methods in subclass is it a mandantory/compulsory so we have to use abstract clas to make it mandatory to use other wise it will gives an error
from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
       
    def perimieter(self):
        pass

class Square(Shape):
    def __init__(self, side):
        self.__side = side
    def area(self):
        return self.__side * self.__side
    def perimeter(self):
        return 4 * self.__side

square = Square(5)
print(square.area())
print(square.perimeter())        

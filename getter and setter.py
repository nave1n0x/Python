#these are used to prevent acces and to private methods and variables to be modified or used

#encapsulation is that which can prevent modification of some methods and variables 
class Speed:
    def __init__(self):
          self.speed = 80
          self.__speed_2 = 100#private varible that can be accesed only inside the class
    def __get_speed(self):
        return self.__speed_2    

sp1 = Speed()
print(sp1.speed)
print(sp1.__get_speed())
      
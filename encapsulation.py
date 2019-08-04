#encapsulation is that which can prevent modification of some methods and variables 
class Speed:
    def __init__(self):
          self.speed = 80
          self.__speed_2 = 100#private varible that can be accesed only inside the class

sp1 = Speed()
sp1.speed = 100
sp1.__speed_2 = 200
print(sp1.speed)
print(sp1.__speed_2)
      
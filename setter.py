#encapsulation is that which can prevent modification of some methods and variables 
class Speed:
    def __init__(self):
          self.speed = 80
          self.__speed_2 = 90#private varible/attribute that can be accesed only inside the class
    def get_speed(self):
        return self.__speed_2
    def set_new_speed(self,new_speed):
        self.__speed_2 = new_speed


sp1 = Speed()
print(sp1.get_speed())
sp1.set_new_speed(100)
print(sp1.get_speed())
      
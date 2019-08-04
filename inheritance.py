class Animal:
    def speak(self):
        print("Animal Speaking")
class Dog(Animal):
    def bark(self):
        print("dog barking")#inheritance
class DogChild(Dog):
    def eating(self):
        print("Eating meat")#multilevel inheritance
d = DogChild()
d.eating()
d.speak()
d.bark()               
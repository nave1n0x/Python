n = input("enter name:")#taken input
a = int(input("enter age"))
m = int(input("enter marks"))

class student:#created a class
    def __init__(self,n,a,m):#created a constructer and also a positional arguments
      self.name = n
      self.age = a
      self.marks = m

    def display(self):#created a display method
      print("Name is :", self.name)
      print("Age :", self.age)
      print("Marks :", self.marks)

s1 = student(n,a,m)#used student class
s1.display()#used display method

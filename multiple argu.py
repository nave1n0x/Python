
class student:#created a class
    def __init__(self,n,a,*m):#created a constructer
      self.name = n
      self.age  = a
      self.marks = m

    def display(self):#created a display method
      print("Name is :", self.name)
      print("Age :", self.age)
      print("Marks :", self.marks)

s1 = student('naveen',18,18,25,14,15,16,200)#used student class
s1.display()#used display method

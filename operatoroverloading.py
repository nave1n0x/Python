class Python:
    def __init__(self,pages):
        self.pages = pages

    def __add__(self,other):#here self means b1 and other means b2
       return self.pages + other.pages

    def __gt__(self,other):
          return self.pages > other.pages

    def __mul__(self,other):
        return self.pages * other.pages

class Java:
    def __init__(self,pages):
        self.pages = pages

b1 = Python(100)
b2 = Java(500)

print(b1 + b2)
print(b1 * b2)
print(b1 > b2)
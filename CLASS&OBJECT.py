class Laptop:#class
  def __init__(self):#function defined by me  and here there are attributes 
    self.name = "hp"
    self.model = "15ay516tx"
    self.ram = "16gb"
    self.proccesor = "amd"

  def action(self):#this is actions related my function and class laptop
        print ("Name -", self.name)
        print ("Model -", self.model)
        print ("Ram -", self.ram)
        print ("Processor - ", self.proccesor)

l1 = Laptop()
print (l1.name)
print (l1.ram)
print (l1.model)
print (l1.proccesor)

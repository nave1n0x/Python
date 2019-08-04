class parent:
    def __init__(self,name):
        print("this first init",name)
class parent2:
    def __init__(self,name1):
        print("this first init",name1)
class child(parent,parent2):
    def __init__(self):
        print("this my second init")
        super().__init__('naveen')
        super().__init__('Naveenkumar')#we are able to print the details by super function int this file
n1 = child()        
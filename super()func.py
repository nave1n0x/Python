# the super function is when an there are two init meathods in that the second will execute what if we want first we can use super function so inthis iam going to tell without using super in next file im going to tell with super()
class parent:
    def __init__(self,name):
        print("this first init",name)
class child(parent):
    def __init__(self):
        print("this my second init")
        parent.__init__(self,'naveen')#we are able to print the details by i=usig this
n1 = child()        
def add(a,b):
    return (a + b)
  
print (__name__)#here you can see that if __name__=="__main__"if name is main then the main code will execute otherwise if any other file is using this module the other functions and statements should not print that why we use name == main here
if __name__=="__main__":
 print (add(5,5))
 

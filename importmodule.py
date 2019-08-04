#from app import mymodule
#import app.mymodule #any type you can use to call a module from diffrent folder
# and the from the diffrent  folder the my module can be the called and we can give a name for the module alos as  below
import app.mymodule as myfun # this we can give aname for our fuction

result=myfun.add(10,200)
print(result)
result1=myfun.multi(10,300)
print(result1)
result2=myfun.divide(10,500)
print(result2)

class summ:
    def summation(self,a,b):
        return a+b;
class multi:
    def multiplication(self,a,b):
        return a*b;
class divide(summ,multi):#multiple base class inheritance
    def derived(self,a,b):
        return a/b;
d = divide()
print(d.summation(10,5))
print(d.multiplication(10,5))
print(d.derived(10,5))                
        
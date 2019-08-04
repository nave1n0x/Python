
class Salary:#here we are making a seen of (has a) like employee haas a salary,library has a book,human has a heart
    def __init__(self, pay, reward):#we initiated the attributes like pay and reward
          self.pay = pay
          self.reward = reward
    def annualsal(self):#here th salary and reward will be added but not printed
        return (self.pay*12) + self.reward;
class employee:#this is employee class
    def __init__(self, name, position,sal):#here the employee attributes are declaredlike postion his name etc
          self.name = name
          self.position = position
          self.annualsalary = sal#here we have created a attribute or object of annual salary because th there are to init construtors are there the second one will be executed so we have taken and created a obj/attribute here to acces the content inside the above init from salary class
    def annual_salary(self):#and we have made a method that is to return the total annual salary method from the salary class
        return self.annualsalary.annualsal()
sal = Salary(100000, 5000)
emp = employee("Naveen", "Py Dev",sal)#details of emmployee predefined here
print(emp.annual_salary())#printiing of the employee salary with his reward here

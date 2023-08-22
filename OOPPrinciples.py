#classes are user defined blueprint or prototype
#sum, multiplication, addition, constant
#methods, class variables, instance variables, constructor
#instance and class variables have whole different purpose

class Calculator:
    num =  100 #class variables

    #default constructor
    #calling constructor in python always should be  __init__
    def __init__(self, a, b):
        self.firstNumber = a
        self.secondNumber = b
        print("I am called automatically when object is created")
                 
    def getData(self):
        print("I am now working")

    def Summation(self):
        return self.firstNumber + self.secondNumber + Calculator.num


obj = Calculator(2, 5) #syntax to create objects in python
obj.getData()
print(obj.Summation())

obj1 = Calculator(7,4)
obj1.getData()
print(obj1.Summation())

#class, objects and constructor
class EmployeeRecords:

    def __init__(self, ID, fname, lname, salary):
        self.ID = ID
        self.fname = fname
        self.lname = lname
        self.salary = salary
        self.email = lname + '.'+ '@testcompany.com'

    def fullname(self):
        return'{} {}'.format(self.fname, self.lname)

emp1 = EmployeeRecords(236, 'Binod', 'Bashyal', 10000)
emp2 = EmployeeRecords(745, 'Sailesh', 'Neupane', 50000)

print(emp1.email)
print(emp2.fname)
print(emp2.fullname())
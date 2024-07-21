#polymorphism

'''2 types->method overridding -same function and different parameter -compile time
method overloading-same function same parameter -runtime '''

class person:
    def __init__(self,name,age):
     self.name=name
     self.age=age
    def __str__(self):
     return f'{self.name} {self.age}'
class student(person):
  def __init__(self,name,roll,age,branch):
     super().__init__(name,age)
     self.roll=roll
     self.branch=branch
  def __str__(self):
     perdetails=super().__str__()
     return f' {perdetails} {self.roll} {self.branch}'
class annualday(student):
   def __init__(self,name,age,roll,branch,program):
    super().__init__(name,age,roll,branch)
    self.program=program
   def __str__(self):
    studetails=super().__str__()
    return f' {studetails} {self.program}'
aobj=annualday('sath',20,'e4','cse','solo')
print(aobj)



    
  
'''class
object
constructur
encapsulation
polymorphism
abraction
inheritance

class-logical entity,structure,blue print of object
class is a keyword.class contains methods/functions,constructors,data. when ever we create class memory is not allocated

object is a real world entity
object is instance/subpart of class ,physical entity
object contains-properties,behaviour,function,identity

constructor-special method/function used to invoke instance variable 
constructor doesnot return any value so dont need to use return 
while creating the object constructor is called implicitly(default)
3 types of constructors 
-> default-default constructor is going to be invoked
->parameterized-with parameter
->not parameterized-without parameter
self-self referable variable 
object is created outside the class
object.display for calling the function'''

#print student details 
'''
class student:
    def __init__ (self,name,rollno,branch,address,email):
           self.name=name
           self.rollno=rollno
           self.branch=branch
           self.address=address
           self.email=email
    def display(self):
          print("name is:",self.name)
          print("rollno  is:",self.rollno)
          print("branch is:",self.branch)
          print("address is:",self.address)
          print("email is:",self.email)
s1=student('sath',1,'cse','hyd','sath@gmail.com')
s1.display()

#name->str->8
#roll->int->4
#branch->str->8,8,8 ->36 bytes->36*  -> memory is allocated for reducing the space-by applying static
# static is ised for the memory management 
#instead of creating individually a common data create a static data and pass the copy to all the objects 


class student:
    branch='cse'#static is used after the class and before the constructor 
    def __init__ (self,name,rollno,address,email):
           self.name=name
           self.rollno=rollno
           self.address=address
           self.email=email
    def display(self):
          print("name is:",self.name)
          print("rollno  is:",self.rollno)
          print("branch:",student.branch)
          print("address is:",self.address)
          print("email is:",self.email)
s1=student('sath',1,'hyd','sath@gmail.com')
s1.display()


class student:
    branch='cse'#static is used after the class and before the constructor 
    def __init__ (self,name,rollno,address,email):
           self.name=name
           self.rollno=rollno
           self.address=address
           self.email=email
    def display(self):
          print("name is:",self.name)
          print("rollno  is:",self.rollno)
          print("branch:",student.branch)
          print("address is:",self.address)
          print("email is:",self.email)
s1=student('sath',1,'hyd','sath@gmail.com')
s2=student('sravya',2,'hyd','sravya@gmail.com')
s1.display()
s2.display()'''

#printing employyye details using static 
'''
class employye:
    project='data enquiry'
    company='accenture'#static is used after the class and before the constructor 
    def __init__ (self,name,rollno,address,email):
           self.name=name
           self.rollno=rollno
           self.address=address
           self.email=email
    def display(self):
          print("name is:",self.name)
          print("rollno  is:",self.rollno)
          print("branch:",employye.company)
          print("project name is:",employye.project)
          print("address is:",self.address)
          print("email is:",self.email)
s1=employye('sath',1,'hyd','sath@gmail.com')
s2=employye('sravya',2,'hyd','sravya@gmail.com')
s1.display()
s2.display()'''
      
#instead of using display we use __str__ to dispalyf ' { to print the value orelse it prints self.name }'

'''class employye:
    project='data enquiry'
    company='accenture'#static is used after the class and before the constructor 
    def __init__ (self,name,rollno,address,email):
           self.name=name
           self.rollno=rollno
           self.address=address
           self.email=email
    def __str__(self):
          return f' {self.name} {self.rollno} {self.address} {self.email}'

s1=employye('sath',1,'hyd','sath@gmail.com')
s2=employye('sravya',2,'hyd','sravya@gmail.com')
print(s1)
print(s2)'''

#abstraction 

#the class which contain abtract and non abstract
#we cannot create an object for an abstract class but we can extend
#to excute an constructor we need to keep paranthesis ()
#for class while we calling an object we dont need use () paranthesis 
#inheritance

'''class JNTU:
    def schedule_acadamic():
        print("scheduling academic")
    def declare_holidays():
        print("national and summer holidays")
    def results():
        print("go to www.jntu.com")
class sridevi(JNTU):
    def fees():
        print("3rd year fees is 85000")
sobj=sridevi
sobj.fees()
sobj.schedule_acadamic()
sobj.results()  

#parent and child

class parents:
    def food():
        print("non veg")
    def intrests():
        print("agriculture")
class child(parents):
    def food():
        print("non veg")
sobj=child
sobj.food()
sobj.intrests()
'''

#abstract method:hidden the implemtion and showing the functionality,no body means abstract->nonabstract=complete class
from abc import ABC#-> abstract CLASS abc->module

#from cse import sath 
'''class RBIBank(ABC):
    def interest():#abstract #we can create abstract method for non  unique values #no implementation
        pass
    def loan():#non abstract#implementation
        print("provide home loan")
class HDFC(RBIBank):
    def interest():
        print('8% interest')
class SBI(RBIBank):
    def interest():
        print('7% interest')
class AXIS(RBIBank):
    def interest():
        print('9% interest')
                   
robj=HDFC          
robj.interest()
robj.loan()
'''
#create vehicle

from abc import ABC
class vehicle(ABC): #abstarct - different
    def Speed():
        pass 
    def Milage():
        pass
    def Model():
        pass 
    def breaks():#non abstract-same
        print('stop the vehicle')
class RangeRover():
    def Speed():
        print('450 max speed')
    def Milage():
        print('12KMPH')
    def Model():
        print('legender')
class Forture():
    def Speed():
        print('380 max speed')
    def Milage():
        print('13KMPH')
    def Model():
        print('thar')
sobj=RangeRover
sobj.Speed()
sobj.Milage()

sobj=Forture
sobj.Speed()
sobj.Model()
        


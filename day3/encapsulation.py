#encapsulation 
'''binding data and methods into the single components 

ex: class is best example of encapsulate
adv
code integration 
security 
'''
#encapsulation using parameter 

class employee:
    def __init__(self,name,role,salary):#constructor
        self.name=name
        self.role=role
        self.__salary=salary# '__' used for private data get_salary -function
    def get_salary(self):  #get_salary -function #public method and data is private
        return self.__salary
    def empdisplay(self):
        print(self.name,self.role)#public method
class company(employee):
    def __init__ (self,cname,loc):
        self.cname=cname
        self.loc=loc
    def comdisplay(employee):
        print(self.cname,self.loc)
    def _hiring(self):
        print('hiring for the manager role')
cobj=company('wipro','gachibowli')# for excuting the constructor we need to keep paranthesis values for class we dont need while calling the objects
eobj=employee('uma','dev',85000)
eobj.empdisplay()
print(cobj._hiring())

#without usoing parameters 

class employee:
    def __init__(self):#constructor
        self.name='sath'
        self.role='dev'
        self.__salary=85000# '__' used for private data get_salary -function
    def get_salary(self):  #get_salary -function #public method and data is private
        return self.__salary
    def empdisplay(self):
        print(self.name,self.role)#public method
class company(employee):
    def __init__ (self,cname,loc):
        self.cname=cname
        self.loc=loc
    def comdisplay(employee):
        print(self.cname,self.loc)
    def _hiring(self):
        print('hiring for the manager role')
 

e1=employee()
e1.empdisplay()
print(e1.get_salary())






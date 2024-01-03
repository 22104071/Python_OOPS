#Destructor
#To destroy the resources tied to the objects
#Destructor is called automatically when object is destroyed.
#
x,y =100,200
# A destructor is used when the reference count is xero and the variable goes out of scope.
#Example: Suppose we use __del__() over the variables x,y and 100,200 being destroyed, now the avriable are of no use, until new values being stored to them, but during their access, some memory is being stored in cache, to destroy that part part too, a destructor is called.

# __new__() is ued to create an object.
# __init__() is used to initialize the object.

import time

class Employee:
    def __init__(self,nm,sal):
        self.name = nm
        self.Salary = sal
        
    def display(self):
        print(f"Name is {self.name} and Salary is {self.Salary}.")
        
    def __del__(self):
        print('Destructor is called.')   
    

emp = Employee('Jay',50000)
emp.display()
temp = emp

del emp
print()
#But there, we stillhave 1 reference count
time.sleep(5)
del(temp)
#Now ref count = 0 , so a destructor get automatically called
#Object is ready for garbage collection.

#Disadvantages:

#1. Circular referencing --> when two objects are pointing each other, like in cyclic inheritance...

import time

class Employee:
    def __init__(self,_nm):
        self.nm = _nm
    
    def __del__(self):
        print('Employee class being called.')
        

print()
class Account:
    def __init__(self,nm):
        self.account = nm
        self.obj = Employee(self)
    
    def __del__(self):
        print('Account class being called')
        
ac = Account(56765)
del ac
time.sleep(4)
#So, here destructor won't work properly, sleep occured first, then deletion.

#2. Exception occur, due to non_exceution of __init__ method.



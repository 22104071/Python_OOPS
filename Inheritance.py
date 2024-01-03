#Deriving a new class from an existing parent class or super class, with all attributes and methods

class Employee: #Parent  class, cannot access child class
    bonus = 2000
    def display(bonus):
        print(bonus) 

print()

class Manager(Employee): # Employee gets inherited as a parent class, can access both classes
    bonus1 = 5000
    def show(self):
        print('class Manager')
        
e1 = Employee()
m1 = Manager()

e1.display()
m1.show()

##print(m1.bonus)
print()
##print(e1.bonus)
#Need of inheritance
#1 Usability
#Examples: 

#Constructor Overriding
#By default, subclass overrides the parent class, along with using its attributes as well as methods...



class Father():
    def __init__(self):
        print('Father constructor called')
        self.vehicle = 'scooter'

class son(Father):
    def __init__(self):
        print('son constructor called')
        self.vehicle = 'BMW' #Now, son class has more prior to father class
    


s = son()  #Father vehicle given to son
print(s.__dict__)

#Super() , to access parent class properties...
r = str(input("RAM:"))
s = str(input("Storage:")) 
print()
class Computer(object):
    def __init__(self):
        self.Ram = r
        self.Storage = s
        
        print("Computer class constructor called")

class Mobile(Computer):
    def __init__(self):
        super().__init__()
        
        self.Model = 'IPhone 15'
        print("Mobile class called")
        
#Apple =Mobile('8gb','512gb')
##print(Apple.__dict__)

# Types of Inheritance
#1. Single inheritance

# one parent one child ex. given above already

#Multi level inheritance

class Model(Mobile):
    def __init__(self):
        super().__init__()
        self.Model = str(input("Model:"))
        self.Color = str(input("Color:"))
        self.Design = str(input("Design:"))
        
# 
year= int(input('Enter the built-year:'))

print()
class Year(Mobile):
    def __init__(self):
        super().__init__()
        self.Year = 2023
        
  
      
print()

Samsung = Model()
Apple_ = Year()


print("Model-driven doc:",Samsung.__dict__,'\n')
print("Year-driven doc:",Apple_.__dict__)  



#Class Hierachy : Computer --> Mobile --> { Model, Year } 


class Computer(Year,Model):
    def __init__(self):
        super().__init__()
        
        
#m = int(input("Enter model year:"))

c1 = Computer()
print(c1.__dict__,'\n')
        
#Class Hierachy : Computer --> Mobile --> { Model, {Year --> Computer} } 

class Mac(Computer):
    def __init__(self):
        super().__init__()
        

M2 = Mac()
print(M2.__dict__)
       
#Class Hierachy : Computer --> Mobile --> { Model, {Year --> Computer --> Mac} }



     




    
    


    



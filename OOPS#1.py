class Employee:
    company_name = "McKinsey"
    #base_salary = int(input("Enter base salary:"))
    
    def __init__(self,sal,age): #Constructor , non-parameterised
        self.salary=sal
        self.age= age
    
    #def __subclasses__(self,sal,age):
     #   return sal,age
    
    def display(self):
        print(f"Salary is:{self.salary} & Age is:{self.age}")

    def change_data(self):
        self.age = int(input('Enter new age:'))
        self.salary = int(input('Enter new salary:'))
    @classmethod
    def get_company_name(cls):
        cls.company_name = 'Amazon'
        print(f"New Company name is",cls.company_name)
        
    def setName(self,name):
        self.name = name
    
    def getName(self,name):
         print(name)
    
    

    @staticmethod
    def Bonus(base_salary):
        _Bonus = base_salary*0.25
        Salary_after_Bonus = base_salary+_Bonus
        print(Salary_after_Bonus)
    
e1 = Employee(24000,29)
e2 = Employee(45000,24)

#print(e1.salary) #To show content as dictionary
#print(e2.display())
e1.salary = 34000 #Updation
#print("Updated Salary:",e1.salary)
#e2.display()

#print('age is:',getattr(e1,'age')) --> Getting the value of attribute
#delattr(e2,'age') --> # Permanent Deletion
#print('\n',Employee.__doc__) --> # Class documentation string
#print(hasattr(e2,'age')) --> #Attribute check
#print(Employee.__module__) --> #module name
#print(Employee.__name__) --> class name
#print(Employee.__dict__) --> #Dictionary of class

#print(isinstance(e1,Employee)) --> #To check obj is related to given class

#Instance variables 
#For Employee, salary and age are insytance variables , and modification will be limited to the one object only.
#Seperate copies created for different object


#e1.base_salary = int(input('Enter employee salary:'))
#print(e1.__dict__) #Adding value outside the class

#e2.change_data()
#print(e2.__dict__)

##Class variables


#These varaibles are created for the entire class, and only one copy exist for the whole class.
#For all objects, and no modification is there is for particular class object.

#print(e1.company_name)
Employee.company_name = 'Deloitte'
#print(Employee.company_name) -->  #Class based reference
e1.company_name = 'JPMC' #Now, it become an instance variable
print(e1.company_name)

#Class method
#cls variable --> class refernce
#Using decorator


Employee.get_company_name()

#Setter (set value for ins_method)and getter (get value for i_m) methods
#These are just conventions, not specific methods by oops

#e1.setName(input('Enter the name:'))



#e2.getName("Hemant")

# Static methods
#Methods that work over external data, not over any class or object
#Can work over class
print()
a = int(input('Enter base salary:'))
print('the Salary after bonus is:')
Employee.Bonus(a)

#ENCAPSULATION

class Employee:
    company_name = "McKinsey"
    
    
    def __init__(self,sal,age): #Constructor , non-parameterised
        self.__salary=sal #private data
        self.age= age #public data
        self.health = 'OK'
        
        
        
    def display(self):
        print(f"Age is {self.age} and salary is {self.__salary}") # Now, private being accessible using methods like setter, getter, etc.
        self.__salary = 40000 # Now, value cannot be changed for private data using such declaration.
         

#object_name.name To obstruct this way of calling data, is the need of encapsulation...

# By making data private,no access as well as outside the class modification can be done.
#It can be achieved using methods...

e1 = Employee(20000,19)
e1.display()
print()

class HR:
    def __init__(self):
        self.number_of_emp = 32
        e1.age =23
        self._Employee_salary = 23000
        
        print("age",e1.age,e1._Employee__salary)

h1 = HR()

 

    
#Now data of age has been modified since the access not restricted from the HR class.
#However, this process of accessing variable outside the called name mangling.
#Here, Employee is apublic variable, that can be accessible everywhere using object reference.

#Using 2 _ before declaring the variables in the class, it can be made private...

print(h1.__dict__)





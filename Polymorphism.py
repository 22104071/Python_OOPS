#Polymorphism is the ability to show multipleforms as per different conditions.
#Example: len on string give no. of characters including symbols, but on list of strings, it will give count of string elements present.
a = len("Hello")
b = len(["A",'B','C'])
print(a,'\t',b)

#

_Speed = int(input('Max Speed:'))   
class Vehicle:
    def __init__(self,name,color,price):
        self.name = name
        self.color = color
        self.price = price
        
    def get_details(self):
        print(f'Name :{self.name}')
        print(f'Color :{self.color}')
        print(f'Price:{self.price}')
        
    
     
    def max_speed(self):
        speed = _Speed
        print(f'The max speed limit is {speed}kmph')
        
    def gear(self):
        speed = speed
        print(f'Gear must down at {speed}kmph')
        

v1 = Vehicle('Truck','Silver',4500000)
print(v1.__dict__)

class Car(Vehicle):
    Speed = 140
    def max_speed(self):
        speed = 140
        print(f'The max speed limit is {speed}kmph')
        
    def gear(self):
        speed = _Speed
        print(f'Gear must down  by 1 at {speed}kmph')
        
C1 = Car('MS Swift','Red',560000)
print(C1.__dict__)
v1.get_details()
v1.max_speed()
print()
C1.get_details()
C1.max_speed()

print()
#####

class Cart:
    def __init__(self,basket1,basket2,basket3):
        self.Clothes = basket1
        self.Electronics = basket2 
        self.Grocery = basket3  
    
    def __len__(self):
        print('The total count of items in the cart:')
        return len(self.Clothes)+len(self.Electronics)+len(self.Grocery)
        #return may result in none if print command was used there, and len() don't return None.

c1 = Cart(['Pants','Shirt','Socks'],['Earphones','TV Console'],['Fruits'])
print(c1) #Magic method __str__ got automatically called, and go to built-in memory then memory location is searched for that memory element...
print(c1.__dict__)
print()
#Polymorphism with functions

class BMW:
    def fuel_type(self):
        print("Diesel")

    def max_speed(self):
        speed = _Speed
        print(f'The max speed limit is {speed}kmph')
        
class Ferrari:
    def fuel_type(self):
        print("Petrol")

    def max_speed(self):
        speed = _Speed*1.8
        print(f'The max speed limit is {speed}kmph')
def car_details(obj):
    obj.fuel_type()
    obj.max_speed()

bmw = BMW()
ferrari = Ferrari()       

car_details(bmw)
print()
car_details(ferrari)
print()
#Operator Overloading

#' +' operator is used as adiition in integers as well as floats, and us eto concatenate strings as well as char and as join in case of lists

num1 = 10
num2 = 20
print(num1+num2)
print(num1.__add__(num2))
print(int.__add__(num2,num1))

#Step one- is to check Data type of left operand
#Step two- going that class 
#Step three- call __add__() f

# Merging types can cause type error.

print(dir(int))

print()

class Book:
    def __init__(self,title,pages):
        self.Title = title
        self.Pages = pages
    
    def __add__(self,other):
        total = self.Pages+other.Pages
         #return total --> for line  132
        return Book('All pages:',total) # return non string here
    
    def __str__(self) -> str:
            return str(self.Pages)
       
b1 = Book("A Suitable Boy",560)
b3 = Book("A Suitable Boy",560)
b2 = Book("The Jungle Book",450)
print("Net pages:",b1.Pages+b2.Pages)
print("Total pages:",b1+b2)    #b1.__add__(b2)     -->Book.__add__(b1,b2)
print()
print("Total pages:",b1+b2+b3)
print()

#

class hotel:
    def __init__(self,name,fare):
        self.Name = name
        self.Fare_per_night = fare
    def __gt__(self,other):
         return self.Fare_per_night>other.Fare_per_night
        
        
h1 = hotel("Taj Hotel",20000)
h2 = hotel("The Lalit",8500)

print(h1.Fare_per_night>h2.Fare_per_night) #True

print(h1<h2) #False
print()

# Method Overloading
#To add same name methods, having different functionality, over different working env. as well as usage.
#In PYTHON, but latest defined method has highest priority than previous ones.(NO PURE METHOD OVERLOADING CONCEPT) 
#To achieve

class calc:
    def add(self,num1=None,num2=None,num3=None):
        if num1!=None and num2!=None and num3!=None:
            print('addition:',num3+num1+num2)
        elif num1!=None and num2!=None:
            print('addition:',num1+num2)
        else:
            print('Incorrect Parameters provided...')
        
c1 = calc()
c1.add(10,20)
c1.add(10,20,390)
print()
#class Area:
    #def area(self,l):
        #print("Area(Square):",l**2)
    #def area(self,b,l):
        #print(f"Area(Reactangle({b},{l})):",l*b)

#
#a.area(2) --> #Expecting area of square, but will won't work as latest expression has two parameters. 


# To achieve method overloading, we will construct one method only

class Area:
    def area(self,l=0,b=None):
        if l>0 and b!=None:
             print(f"Area(Reactangle({b},{l})):",l*b) 
        elif l>0 and b==None:
            print(f"Area(Square({l})):",l**2) 
a = Area()
a.area(2)     
a.area(9,7)   
                 







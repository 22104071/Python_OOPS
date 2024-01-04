
x = 100
class Z:
    def __init__(self,a,b):
         print(a*b)
    def add(self,a,b):
        return a+b
    def __call__(self,a,b): # __call__() magic method
        print('Hello')
        return a+b
    
    
def add(a,b):
        return a+b
print(type(add))
#Functions are callable methods but integers are not callables. unless private
#callable is an in_built f(x) to check if the object is callable or not.
print(callable(x)) #int  --> False
print(callable(add)) #F(x) --> True
print(add(10,56))
print(add.__call__(10,20)) #Call method is defined in funtion add.

z1 = Z(3,55)

print(callable(z1)) ## Object is not callable
print(callable(Z)) # Class is always callable
#To make object z1 callable, we need to create a method __call__() in their class, (in line 7,8).
print(z1(67,89)) #Here inner class function add is not called..., unless specified.


class Decorator(object):
    def __init__(self,func):
        self.function = func
    
    def __call__(self,a,b):
        #original func
        result = self.function(a,b)
        #square
        return result**2        

#It is a class decorator, to return the function valkue without there being a modification in the class.
#It is used to replace line 16 snippet.
@Decorator
def add(a,b):  
    return a+b
print('Square of sum of two nos.=',add(2,4))
#add = Decorator(add)
#print(,add(10,20)) #add.__call__(a,b)

#######---------------------------------------------------------->>

class  Decorator(object):
    def __init__(self,func):
        self.function = func
    
    def __call__(self,*args):
        try:
            
            if any([isinstance(i,str) for i in args]): #[F,T,F] , IF ANYONE IS True
                raise TypeError("Cannot pass string as arguments")
            else:
                return self.function(*args)
        except Exception as obj:
            print(obj)

@Decorator
def add(*args):
    sum1 = 0
    for num in args:
        sum1= sum1+num
    return sum1


print(add(10,20,30)) 
print(add(10,'20',30))

add = Decorator(add)
print()
add(10,'20',30) #add.__call__() #Method call
print()
add(10,20,30)

#Property decorator
#Use to generate setter,getter and deleter methods(in_built)


    
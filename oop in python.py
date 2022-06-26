#oop in python

#making class by class keyword

#simple clases
class Dog:
    
	# class attribute
	attr1 = "mammal"

	# Instance attribute
	def __init__(self, name):
		self.name = name

# Object instantiation
Rodger = Dog("Rodger")
Tommy = Dog("Tommy")

# Accessing class attributes
print("Rodger is a {}".format(Rodger.__class__.attr1))
print("Tommy is also a {}".format(Tommy.__class__.attr1))

# Accessing instance attributes
print("My name is {}".format(Rodger.name))
print("My name is {}".format(Tommy.name))

#inheritance

# parent class
class Person(object):
 
    # __init__ is known as the constructor
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber
 
    def display(self):
        print(self.name)
        print(self.idnumber)
         
    def details(self):
        print("My name is {}".format(self.name))
        print("IdNumber: {}".format(self.idnumber))
     
# child class
class Employee(Person):
    def __init__(self, name, idnumber, salary, post):
        self.salary = salary
        self.post = post
 
        # invoking the __init__ of the parent class
        Person.__init__(self, name, idnumber)
         
    def details(self):
        print("My name is {}".format(self.name))
        print("IdNumber: {}".format(self.idnumber))
        print("Post: {}".format(self.post))
 
 
# creation of an object variable or an instance
a = Employee('Rahul', 886012, 200000, "Intern")
 
# calling a function of the class Person using
# its instance
a.display()
a.details()


#Polymorphism

class Bird:
    
	def intro(self):
		print("There are many types of birds.")

	def flight(self):
		print("Most of the birds can fly but some cannot.")

class sparrow(Bird):

	def flight(self):
		print("Sparrows can fly.")

class ostrich(Bird):

	def flight(self):
		print("Ostriches cannot fly.")

obj_bird = Bird()
obj_spr = sparrow()
obj_ost = ostrich()

obj_bird.intro()
obj_bird.flight()

obj_spr.intro()
obj_spr.flight()

obj_ost.intro()
obj_ost.flight()


#encapsulation
# Python program to
# demonstrate private members

# Creating a Base class
class Base:
	def __init__(self):
		self.a = "Hamza"
		self.__c = "Hamza"

# Creating a derived class
class Derived(Base):
	def __init__(self):

		# Calling constructor of
		# Base class
		Base.__init__(self)
		print("Calling private member of base class: ")
		print(self.__c)


# Driver code
obj1 = Base()
print(obj1.a)

# Uncommenting print(obj1.c) will
# raise an AttributeError

# Uncommenting obj2 = Derived() will
# also raise an AtrributeError as
# private member of base class
# is called inside derived class

#data hiding

class MyClass:
    
	# Hidden member of MyClass
	__hiddenVariable = 0
	
	# A member method that changes
	# __hiddenVariable
	def add(self, increment):
		self.__hiddenVariable += increment
		print (self.__hiddenVariable)

# Driver code
myObject = MyClass()	
myObject.add(2)
myObject.add(5)

# This line causes error
print (myObject.__hiddenVariable)


#printing object
class Test:
    def __init__(self, a, b):
        self.a = a
        self.b = b
  
    def __repr__(self):
        return "Test a:%s b:%s" % (self.a, self.b)
  
    def __str__(self):
        return "From str method of Test: a is %s," \
              "b is %s" % (self.a, self.b)
  
# Driver Code        
t = Test(1234, 5678)
print(t) # This calls __str__()
print([t]) # This calls __repr__()


# Python example to check if a class is
# subclass of another

class Base(object):
	pass # Empty Class

class Derived(Base):
	pass # Empty Class

# Driver Code
print(issubclass(Derived, Base))
print(issubclass(Base, Derived))

d = Derived()
b = Base()

# b is not an instance of Derived
print(isinstance(b, Derived))

# But d is an instance of Base
print(isinstance(d, Base))


# Python example to show that base
# class members can be accessed in
# derived class using base class name
class Base(object):

	# Constructor
	def __init__(self, x):
		self.x = x	

class Derived(Base):

	# Constructor
	def __init__(self, x, y):
		Base.x = x
		self.y = y

	def printXY(self):
	
	# print(self.x, self.y) will also work
	print(Base.x, self.y)


# Driver Code
d = Derived(10, 20)
d.printXY()


# Python example to show that base
# class members can be accessed in
# derived class using super()
class Base(object):

	# Constructor
	def __init__(self, x):
		self.x = x	

class Derived(Base):

	# Constructor
	def __init__(self, x, y):
		
		''' In Python 3.x, "super().__init__(name)"
			also works'''
		super(Derived, self).__init__(x)
		self.y = y

	def printXY(self):

	# Note that Base.x won't work here
	# because super() is used in constructor
	print(self.x, self.y)


# Driver Code
d = Derived(10, 20)
d.printXY()


# Python program to demonstrate
# use of class method and static method.
from datetime import date


class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	# a class method to create a Person object by birth year.
    #Class method can access and modify the class state.
    #The class method takes the class as parameter to know about the state of that class.
	@classmethod
	def fromBirthYear(cls, name, year):
		return cls(name, date.today().year - year)

	# a static method to check if a Person is adult or not.
    #Static Method cannot access or modify the class state.
    #Static methods do not know about class state. These methods are used to do some utility tasks by taking some parameters.
	@staticmethod
	def isAdult(age):
		return age > 18


person1 = Person('mayank', 21)
person2 = Person.fromBirthYear('mayank', 1996)

print(person1.age)
print(person2.age)

# print the result
print(Person.isAdult(22))

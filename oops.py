'''oops concept pillars:
1.Inheritance: The ability of a new class (child class) to inherit properties and behaviors from an existing class (parent class).
2.Encapsulation: The bundling of data and methods that operate on that data within a single unit (class), and restricting access to some of the object's components.
3.Polymorphism: The ability of different classes to be treated as instances of the same class through a common interface, often achieved through method overriding.
4.Abstraction: The concept of hiding the complex implementation details and showing only the necessary features of an object, allowing the user to interact with it at a higher level.'''


class Animal:
    def __init__(self,name):
        self.name = name
    def info(self):
        print("Animal:",self.name)

class Dog(Animal):
    def __init__(self,name,breed):
        super().__init__(name)
        self.breed = breed
    def details(self):
        print(self.name,"is a",self.breed)

d = Dog("Buddy","Golden Retriever")
d.info()
d.details()

'''types of inheritance:
1. Single Inheritance: A child class inherits from a single parent class.
2. Multiple Inheritance: A child class inherits from more than one parent class.
3. Multilevel Inheritance: A child class inherits from a parent class, which in turn inherits from another parent class.
4. Hierarchical Inheritance: Multiple child classes inherit from a single parent class.
5. Hybrid Inheritance: A combination of two or more types of inheritance.'''

#single inheritance
class Parent:
    def func1(self):
        print("This is function one")
class Child(Parent):
    def func2(self):
        print("This is function two")

c=Child()
c.func1()
c.func2()

#multiple inheritance - 2 parent classes with one child class
class Mother:
    mothername = ""
    def mother(self):
        print(self.mothername)

class Father:
    fathername =""
    def father(self):
        print(self.fathername)

class Son(Mother,Father):
    def parents(self):
        print("Father:",self.fathername)
        print("Mother:",self.mothername)

s = Son()
s.fathername ="John"
s.mothername = "Jane"
s.parents()

#multilevel inheritance - 1 parent class with 1 child class and 1 grandchild class
class Grandfather:
    def __init__(self,grandfathername):
        self.grandfathername = grandfathername

class Father(Grandfather):
    def __init__(self,fathername,grandfathername):
        super().__init__(grandfathername) #Grandfather.__init__(self,grandfathername)
        self.fathername =fathername
class Son(Father):
    def __init__(self,sonname,fathername,grandfathername):
        super().__init__(fathername,grandfathername)  #Father.__init__(self,fathername,grandfathername)
        self.sonname = sonname
    def print_name(self):
        print("Grandfather:",self.grandfathername)
        print("Father:",self.fathername)
        print("son:",self.sonname)

s=Son("Michael","John","Robert")
s.print_name()
print(s.grandfathername)

#hierarchical inheritance - 1 parent with multiple child classes

class Parent:
    def name(self):
        print("This is the parent class")
class Child1(Parent):
    def name1(self):
        print("This is child class 1")
class Child2(Parent):
    def name2(self):
        print("This is child class 2")
c1 = Child1()
c2 = Child2()
c1.name()
c1.name1()
c2.name()
c2.name2()

#hybrid class - combination of two or more classes
class A:
    def func1(self):
        print("This is the parent class of B")
class C:
    def func2(self):
        print("This is the parent class of B")
class B(A,C):
    def func3(self):
        print("This is child class of A and C and Parent of F")
class E:
    def func4(self):
        print("This is the parent class of G")
class F(B,E):
    def func5(self):
        print("This is the child class of B  and E")
class G(E):
    def func6(self):
        print("This is the child class of E")

b = B()
b.func1()
b.func2()
b.func3()
f = F()
f.func3()
f.func4()
f.func5()
g = G()
g.func4()
g.func6()

'''polymorphism - allows functions or methods with same name
 to work differently based on the object that is calling them.
 
 types of polymorphism:
 1. compile-time polymorphism (method overloading): The ability to define multiple methods with the same name 
 but different parameters within the same class.
 2. runtime polymorphism (method overriding): The ability of a subclass to provide a specific implementation of a method 
 that is already defined in its superclass.

 behaviour of the method is decided while program is running  based on the object calling it.
 a child class provides its own version of a method defined in the parent class.


 real time example of polymorphism::
 pay has credit card ,upi etc
 '''

#compile time polymorphism - method overloading
class Calculator:
    def multiply(self,a=1,b=1,*args):
        result  = a * b
        for num in args:
            result *= num
        return result
c = Calculator()
print(c.multiply())
print(c.multiply(2))
print(c.multiply(2,3))
print(c.multiply(2,3,4))

#runtime polymorphism - method overriding
class Animal:
    def sound(self):
        return "some sound"
class Dog(Animal):
    def sound(self):
        return "woof"
class Cat(Animal):
    def sound(self):
        return "meow"
a= [Dog(),Cat(),Animal()]
for i in a:
    print(i.sound())

'''encapsulation - binding the data and methods into single unit
and restricting access to some of the object's components. 
It is achieved through access modifiers:
1. Public: Members are accessible from anywhere.
2. Protected: Members are accessible within the class and its subclasses (conventionally denoted by a single underscore _).
3. Private: Members are accessible only within the class (denoted by a double underscore __).
'''
class BankAccount:
    def __init__(self):
        self.balance = 1000
    def _show_balance(self):              #protected method
        print(f"Balance: {self.balance}")
    def __update_balance(self,amount):    #private method
        self.balance += amount
    def deposit(self,amount):
        if amount > 0:
            self.__update_balance(amount)     #accessing private method within the class
            self._show_balance()
        else:
            print("Invalid amount")
class ShowBalance(BankAccount):
    def display_balance(self):
        self._show_balance()      #accessing protected method from parent class

account = BankAccount()
account.deposit(500)
account._show_balance()  #accessing protected method from outside the class (not recommended)   

'''getter and setter methods are used to modify the value of
private attributes safely.
Instead of accessing directly,these methods provide controlled access'''

class Employee:
    def __init__(self):
        self.__salary = 50000
    def get_salary(self):
        return self.__salary
    def set_salary(self,amount):
        if amount > 0:
            self.__salary = amount
        else:
            print("Invalid salary amount")
emp = Employee()
print(emp.get_salary())
emp.set_salary(60000)
print(emp.get_salary())

'''Abstraction - hiding all the complex implementation and showing only essential features'''
#Abstract Base class - used to acheive data abstraction by defining common interface to its subclasses
# abstract classes are created using abc module and @abstractmethod decorator
from abc import ABC,abstractmethod
class Greet(ABC):
    @abstractmethod
    def say_hello(self):
        pass
class English(Greet):
    def say_hello(self):
        return "Hello!"
    
g = English()
print(g.say_hello())


""" components of Abstraction:
1. Abstract methods: Methods that are declared in the abstract class but do not have an implementation. They must be implemented by the subclasses.
2. concrete methods: methods are fully implemented in the abstract class and can be used by the subclasses without modification.
3. Abstract properties: Properties that are declared in the abstract class but do not have an implementation. They must be implemented by the subclasses.
4. Concrete properties: Properties that are fully implemented in the abstract class and can be used by the subclasses without modification.
5. Abstract classes: Classes that cannot be instantiated and are meant to be subclassed. They can contain both abstract and concrete methods and properties.
6. Interfaces: A special type of abstract class that defines a contract for what methods a class must implement, without providing any implementation itself. In Python, interfaces can be created using abstract base classes."""

from abc import ABC,abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
class Car(Vehicle):
    def start(self):
        return "Car is starting"
class Bike(Vehicle):
    def start(self):
        return "bike is starting"
c= Car()
b= Bike()
print(c.start())
print(b.start())

#static method - a method that belongs to the class rather than an instance of the class. It can be called on the class itself without creating an instance(object).
class Maths:
    @staticmethod
    def add(a,b):
        return a+b
result = Maths.add(5,3)
print(result)
"""
Inheritance: When one class(child/derived) derives the properties
& methods of another class(parent/base).

Types of Inheritance : 
1. Single Inheritance
2. Multi-Level Inheritance 
3. Multiple Inheritance
"""

class Car:
    @staticmethod
    def start():
        print("Car Started..")
    @staticmethod
    def stop():
        print("Car Stopped.")

class ToyotaCar(Car): # inheritance : inherit attrr or method from Car(parent) class [Single Inheritance]
    def __init__(self, brand):
        self.brand = brand

class Fortuner(ToyotaCar): # Multi-Level Inheritance : inhert the properties and methods from these class [Base Class(Car) -> ToyotaCar]
    def __init__(self, type):
        self.type = type

# ---------------------------------------------------------------------------
CAR1 = Fortuner("Diesel")
# CAR1.start()
# ---------------------------------------------------------------------------
car1 = ToyotaCar("fortuner")
car2 = ToyotaCar("prius")
# ---------------------------------------------------------------------------
# print(car1.name)
# car1.start()
# ---------------------------------------------------------------------------

class A:
    varA = "Welcome to class A"

class B:
    varB = "Welcome to class B"

class C(A, B): # Multiple Inheritance : inherit properties/ attr & methods from multiple Parent classes
    varC = "Welcome to class C "

c1 = C()
print(c1.varC)
print(c1.varA)
print(c1.varB)
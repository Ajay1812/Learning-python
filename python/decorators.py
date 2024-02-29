# @staticmethod : static method can't access or modify class state & generally for utility. 
# @classmethod :  A class method is bound to the class & receives the class as an implicit first argument.

"""
1. Static Method
2. Class Method (cls)
3. Instance Method (self) 
"""

class Person:
    name = "anonymous"

    # def changeName(self, name):
    #     # self.name = name
    #     # Person.name = name 
    #     self.__class__.name = name  

    @classmethod 
    def changeName(cls, name): # it will change the name of the Person class directly
        cls.name = name


p1 = Person()
# print(p1.name)
# p1.changeName("Rohit Kumar")
# print(p1.name) # Rohit Kumar : create new instance 
# print(Person.name) 

# @property decorator

class Student:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math
        # self.percentage = str((self.phy + self.chem + self.math) / 3 ) +  "%"

        # Add percentage
    # def calculatePercentage(self):
    #     self.percentage = str((self.phy + self.chem + self.math) / 3 ) +  "%"

    @property 
    def percentage(self):
        return str((self.phy + self.chem + self.math) / 3 ) +  "%"

st1 = Student(98,99,91)
print(st1.percentage)

st1.phy = 90
print(st1.phy) # marks change 
# st1.calculatePercentage() #after running this function will get latest percentage % but when we use @property it will calculate the percentage automatically.
print(st1.percentage) # but percentage is already set according to previous value. 
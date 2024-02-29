# class Student:
#     name = "Ajay"

# s1 = Student()
# print(s1.name)

# s2 = Student()
# print(s2.name)


class Car:
    # def __init__(self): # default constructor
    #     pass

    # --------------------------------------------------------------------
    # class attribute occupy single memory space but when we use self.variable name it will create new memory for variable
    factory_name = "TATA"  # class attr

    # self is the refernce of current object/instance of the class. 
    def __init__(self, instructor, brand, color) -> None: # parameterized constructor : it will run automatically at the object creation state. 
        # print(self)
        self.instructor = instructor
        self.brand = brand  # obj attr > class attr ( if the name of variable same in both places)
        self.color = color
        print("Adding new Car in DB...")
    
    def welcome_instructor(self):
        print("Welcome,", self.instructor)


c1 = Car("Ajay","Mercedes", "black")
# print(c1.instructor)
c1.welcome_instructor()
print(c1.brand)
print(c1.color)

c2 = Car("Rohit","BMW", "blue")
# print(c2.instructor)
c2.welcome_instructor()
print(c2.brand)
print(c2.color)

print(c2.factory_name) # TATA
print(Car.factory_name) # TATA
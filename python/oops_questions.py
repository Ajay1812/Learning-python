class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def areaCirle(self):
        return (22/7) * (self.radius ** 2)

    def perimeterCircle(self):
        return 2 * (22/7)* self.radius

c1 = Circle(21)
# print(c1.areaCirle())
# print(c1.perimeterCircle())

class Employee:
    def __init__(self, role, dept, sal):
        self.role = role
        self.dept = dept
        self.sal = sal

    def showDetails(self):
        print("Role:", self.role)
        print("Department:", self.dept)
        print("salary:", self.sal)

class Engineer(Employee):

    def __init__(self, name,age):
        self.name = name
        self.age = age
        super().__init__("Emgineer", "IT", "8300000")
        print("Name of Employee: ", self.name)
        print("Employee Age: ", self.age)


# e1 = Engineer("Ajay", 23)
# e1.showDetails()

class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price

    def __gt__(self, ord2):
        return self.price > ord2.price 
        

odr1 = Order ("chips", 20)
odr2 = Order("tea", 15) 

print(odr1>odr2)
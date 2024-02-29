
""" OOPS 
1. Abstraction : Hiding the implementation details of a class 
                    and only showing the essential features to the user.
2. Encapsulation: Wrapping data and functions into a single unit
3. Inheritance: When one class(child/derived) derives the properties & methods of another class(parent/base).
4. Polymorphism:
"""

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    
    @staticmethod # decorators : Methods that don't use the self parameter (work at class level)
    def hello(): # self work on object level
        print("Hello Everyone")

    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum+=val
        print("Hi", self.name,  "your avg score is ", round(sum/3 , 2))



s1 = Student("Tony Stark", [99,100,99])
s1.hello()
s1.get_avg()

s1.name = "Iron man"
s1.get_avg()


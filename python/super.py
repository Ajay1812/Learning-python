class Car:

    def __init__(self, type):
        self.type = type
    
    @staticmethod
    def start():
        print("Car Started..")
    @staticmethod
    def stop():
        print("Car Stopped.")

class ToyotaCar(Car):
    def __init__(self, name, type):
        super().__init__(type) # super() is used to access methods and attributes from a parent class within a subclass.
        self.name= name
        super().start()

car1 = ToyotaCar("Prius", "Electric")
print(car1.type)
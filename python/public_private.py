class Account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass # self.__varablename treated as private attr, it means you cant access the attr from outside class
        
    def reset_pass(self):
        print(self.__acc_pass)



cus1 = Account("12345", "qwerty1234")
# print(cus1.acc_no)
# print(cus1.__acc_pass) # cant access  

# cus1.reset_pass()


class Person:
    __name = "anonymous"

    def __hello(self): # we can private our method too
        print("Hello Person!")

    def welcome(self):
        self.__hello()        

p1 = Person()
# p1.__hello()
p1.welcome()
class Account:
    def __init__(self, name, accno, bal):
        self.name = name
        self.accno = accno
        self.bal = bal
    
    def credit(self, amount):
        self.amount = amount
        self.bal += amount
        print("Hi,",self.name,"Amount: Rs.", self.amount, "Credited in your Account Number:", self.accno, "Total Balance:", self.show_bal())
        
    def debit(self,amount):
        self.amount = amount
        self.bal -= amount
        print("Hi,",self.name,"Amount: Rs.", self.amount, "Debit from your Account Number:", self.accno, "Total Balance: ", self.show_bal())

    def show_bal(self):
        # print("Hi,",self.name, " Your Balance:", self.bal) 
        return self.bal

customer1 = Account("Ajay",123, 45000)
customer1.debit(10000)
customer1.show_bal()

customer2 = Account("Rohit", 345, 100000)
customer2.credit(15000)
customer2.show_bal()

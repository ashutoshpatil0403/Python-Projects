class User():
    def __init__(self,name,age,accountno):
        self.name=name
        self.age=age
        self.accountno=accountno

    def show_Details(self):
        print("Personal Details")
        print("Name :",self.name)   
        print("Age :",self.age)  
        print("accountno :",self.accountno) 

#Child Class======================

class Bank(User):
    def __init__(self, name, age, accountno):
        super().__init__(name, age, accountno)
        self.balance=0

    def deposits(self,amount):
        self.amount=amount
        self.balance=self.balance+self.amount
        print(f"Account Balance Has Been Updated to :{self.balance}Rs")

    def Withdrawals(self,amount):
        self.amount=amount
        if self.amount > self.balance:
            print(f"Insufficient Funds ! Balance Available :{self.balance}Rs")
        else:
            self.balance = self.balance - self.amount
            print(f"Account Balance Has Been Updated to :{self.balance}Rs")    

    def view_balance(self):
        self.show_Details()
        print(f"Account Balance :{self.balance}Rs")

    def fixed_deposit(self,amount,time):
        self.amount=amount
        self.time=time
        self.balance=self.amount*time*7.05/100
        print(f"Total Money After {self.time} Year/Years is :{self.balance}Rs")    

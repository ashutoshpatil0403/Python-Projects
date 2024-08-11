print("Hello Welcome to Apna Bank")
#Parent Class=================
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

print("Welcome To Apna Bank")
name=input("Please Enter Your Name :")
age=int(input("Please Enter Your Age :"))
accountno=int(input("Please Enter Your Account Number :"))

User_Details=Bank(name,age,accountno)        
  
#print("Choose Following Options To Proceed....")
#print("1: View Account Balance")
#print("2: Deposit Amount ")
#print("3: Withdraw Amount ")

#User_choice1=int(input('Enter Your Choice From Above Three "1" or "2" or "3"'))
while(True):
    print("Choose Following Options To Proceed....")
    print("1: View Account Balance")
    print("2: Deposit Amount ")
    print("3: Withdraw Amount ")
    print("4: Fixed Deposit ")
    User_choice1=int(input('Enter Your Choice From Above Three "1" or "2" or "3" or "4"'))
    if User_choice1 == 1:
        User_Details.view_balance()
        
    elif User_choice1 == 2:
        amount=int(input("Please Enter The Amount You Want To Deposit :"))
        User_Details.deposits(amount)    
        
    elif User_choice1 == 3:
        amount=int(input("Please Enter The Amount You Want To Withdraw :"))  
        User_Details.Withdrawals(amount)

    elif User_choice1 == 4:
        amount=int(input("Please Enter The Amount You Want To Fixed Deposit:"))  
        time=int(input("Please Enter The Number Of Years You Want To Fixed Deposit:")) 
        User_Details.fixed_deposit(amount,time)   
        
    else:
        print("Please Enter From 1 to 3 Options") 

    print('Press "q" to quit and press "c" to continue')
    
    user_choice2=()
    while(user_choice2!="q" and user_choice2!="c"):
        user_choice2=input()

        if user_choice2=="q":
            exit()
        
        elif user_choice2=="c":
            continue
         

       

#A=Bank("Ashutosh",24,"Male")
#A.show_Details()
#A.deposits(10000)
#A.Withdrawals(2300)
#A.Withdrawals(10000)
#A.view_balance()
#ashutosh=User("Ashutosh",24,"Male")
#ashutosh.show_Details() 
         






































class Currency_Convertor:
    def __init__(self,Rupees):
        self.Rupees=Rupees
        print(f"You Entered Rupees {self.Rupees} Only")

    def USA_Dollar(self):
        self.Dollar=0.012*self.Rupees
        print(f"Your {self.Rupees} Rupees in Dollar is {self.Dollar} $$") 

    def UAE_Dirham(self):
        self.Dirham=0.044*self.Rupees
        print(f"Your {self.Rupees} Rupees in Dirham is {self.Dirham} Dirham") 
    
    def Saudi_Riyal(self):
        self.Riyal=0.045*self.Rupees
        print(f"Your {self.Rupees} Rupees in Riyal is {self.Riyal} Riyal")

    def Russian_Ruble(self):
        self.Ruble=1.10*self.Rupees
        print(f"Your {self.Rupees} Rupees in Ruble is {self.Ruble} Ruble")

    def Japanese_Yen(self):
        self.Yen=1.87*self.Rupees
        print(f"Your {self.Rupees} Rupees in Yen is {self.Yen} Yen")

    def EURO(self):
        self.Euro=0.011*self.Rupees
        print(f"Your {self.Rupees} Rupees in EURO is {self.Euro} EURO")

    def Chinese_Yuan(self):
        self.Yuan=0.085*self.Rupees
        print(f"Your {self.Rupees} Rupees in Yuan is {self.Yuan} Yuan")

#c_c=Currency_Convertor()
print("Welcome To Free Currency_Convertor ")
while True:
    print("1 : USA_Dollar $$")     
    print("2 : UAE_Dirham")   
    print("3 : Saudi_Riyal")   
    print("4 : Russian_Ruble")   
    print("5 : Japanese_Yen")   
    print("6 : EURO")   
    print("7 : Chinese_Yuan")        

    Rs=int(input("Enter Indian Rupees That You Want To Convertor ::"))       
    c_c=Currency_Convertor(Rs)  
    User_Choice1=int(input("PLease Enter Choice By Which You Want To Convert Your Rupees ::"))

    if User_Choice1==1:
        c_c.USA_Dollar()

    elif User_Choice1==2:
        c_c.UAE_Dirham()

    elif User_Choice1==3:
        c_c.Saudi_Riyal()

    elif User_Choice1==4:
        c_c.Russian_Ruble()

    elif User_Choice1==5:
        c_c.Japanese_Yen()

    elif User_Choice1==6:
        c_c.EURO()

    elif User_Choice1==7:
        c_c.Chinese_Yuan()
    else:
        print("Please Enter Valid Choice From 1 to 7")        

    User_Choice2=input("Press q to exit and press c for continue...")
    if User_Choice2=="q":
        print("Thanks For Using Our Free Currency_Convertor")
        break
        #exit()
    elif User_Choice2=="c":
        continue        
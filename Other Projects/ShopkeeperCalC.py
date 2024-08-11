import math
print('Welcome to "Sidhheshwar_Kirana_Stores"')
Sum=0
while(True):
    userinput=input("Enter the Item_Price or Press Q to quit")
    if userinput!="q":
        Sum += int(userinput)
        GST=Sum*0.18
        print(f"Order total so far with GST ::{math.floor(Sum+GST)}/Rs")
    else:
        print(f"Your Total Bill is ===>>>{math.floor(Sum+GST)}.Total GST Paid is 18% i.e {GST}RS\nThanks For Shopping With Us")
        print(f"Total GST Paid is 18% i.e {GST}RS")
        print("Thanks ! Visit Again !")


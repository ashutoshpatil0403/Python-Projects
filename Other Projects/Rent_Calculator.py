rent=input("Enter hostel/flat rent :")
food=input("Enter the amount of food expances :")
electricity_Cost=input("Enter total electricity total cost :")
makkal=int(input("How many people you are living in the hostel/flat :"))
r=int(rent)
f=int(food)
e=int(electricity_Cost)

total_Cost_perhead=(r+f+e)/makkal

print(f"Total Cost per head is {total_Cost_perhead}Rs")
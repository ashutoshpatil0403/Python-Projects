a=int(input("Enter The First Number :"))
b=int(input("Enter The Second Number :"))

Maximum_Number=max(a,b)
#print(Maximum_Number)

while True:
    if Maximum_Number%a==0 and Maximum_Number%b==0:
        break
    Maximum_Number += 1  #Maximum_Number=Maximum_Number+1

print(f"The LCM of {a} and {b} is {Maximum_Number}")
    
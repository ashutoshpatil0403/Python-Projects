secure=(('a','@'),('s','$'),('i','1'),('o','*'),('h','#'),('p','%'),('1','!'),('q','?'))

def securepassword(password):
    for a,b in secure:
        password=password.replace(a,b)
    return password    

password=input("Enter Your Password :")
password=securepassword(password)
print(f"Your Updated Secure Password is {password}")
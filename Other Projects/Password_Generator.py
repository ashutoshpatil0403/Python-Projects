print("Welcom to the worlds top secure pasword providers.....!")
import string
import random

s1=list(string.ascii_lowercase)
s2=list(string.ascii_uppercase)
s3=list(string.digits)
s4=list(string.punctuation)

plenght=int(input("Enter Password Length :"))
s=[]
s.extend(s1)
s.extend(s2)
s.extend(s3)
s.extend(s4)
#print(s)
random.shuffle(s)
#print(s)
print("".join(s[0:plenght]))
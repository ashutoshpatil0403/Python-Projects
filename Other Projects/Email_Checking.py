print("!===========================Right / Wrong Email ID Checking=================!")
email=input("Enter Your Email :")
k=0
if len(email)>=6:
    if email[0].isalpha():
        if ("@" in email) and (email.count("@")==1):
            if (email[-3]==".") ^ (email[-4]=="."):
                print("Right Email ID")
                #for i in email:
                    #if i==i.isspace():
                      #  k+=1
                #if k>=1:
                 #   print("Wrong Email 5")
                #else:    
                  #  print("Right Email ID") 
                          
            else:
                print("Wrong Email ID 4")
        else:
            print("Wrong Email ID 3")
    else: 
        print("Wrong Email ID 2")
else:
    print("Wrong Email ID 1 ")
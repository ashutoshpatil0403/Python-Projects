#print('Welcome to "!===Saraswati_Library===!"')

class Library:
    def __init__(self,booklist,name):
        self.booklist=booklist
        self.name=name
        self.lenddict={}

    def displaybook(self):
        print(f"We have a following books in our library :{self.name}")
        for book in self.booklist:
            print(book)

    def lendbook(self,user,book):
        if book not in self.lenddict.keys():
            self.lenddict.update({book:user}) #Lenddict means means books that are given to read some other user
            print(f"Lender-Book database has been updated .You can take book now")
        else:
            print(f"The book is already being used by {self.lenddict[book]}")    
    
    def addbook(self,book):
        self.booklist.append(book)
        print("Book has been added to the booklist")    

    def returnbook(self,book):
        self.lenddict.pop(book)
 
Ashu=Library(["Polity:M.Laxmikant","Modern-History:Bipin_Chandra","Ancient-Medieval-History:Upindar Singh","11-12th NCERT Economy","11-12th NCERT Geography"],"Saraswati_Library")
while(True):
    print(f"Welcome to the {Ashu.name}")
    print("Enter your choice to continue: \n1:Display Book\n2:Lend a Book\n3:Add a Book\n4:Return a Book")
    user_choice=int(input())
    if user_choice==1:
        Ashu.displaybook()

    elif user_choice==2:
        book=input("Enter the name of book you want to lend:")
        user=input("Enter your name")
        Ashu.lendbook(user,book)

    elif user_choice==3:
        book=input("Enter the name of the book you want to add")
        Ashu.addbook(book)
    
    elif user_choice==4:
        book=input("Enter the name of the book you want to return")
        Ashu.returnbook(book)

    else:
        print("Not a valid option")

    print('Press "q" to quit and press "c" to continue')
    user_choice2=()
    while(user_choice2!="q" and user_choice2!="c"):
        user_choice2=input()

        if user_choice2=="q":
            exit()
        
        elif user_choice2=="c":
            continue

            









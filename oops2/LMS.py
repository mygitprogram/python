class library:
    booklist=[]
    def __init__(self,list):
        self.booklist = list
        self.lendbookslist =[]
      
    def addbooks(self,bname):
        self.booklist.append(bname)
        print("books added")
    def displaybooks(self):
        print("the list of books are")
        for i in self.booklist:
            print(i)
    def lendbooks(self,bname):
        if bname in self.booklist:
            self.lendbookslist.append(bname)
            self.booklist.remove(bname)
            print(bname," lended to you")
        else:
            if bname in self.lendbookslist:
                print("Book already lended")
            else:
                print("Book not in the Library")
    def returnbooks(self,bname):
        if bname in self.lendbookslist:
            self.lendbookslist.remove(bname)
            self.booklist.append(bname)
            print("Thanks for returning the books")
        else:
            if bname in self.booklist:
                print(bname,"not lended.It is with us")
            else:
                print(bname,"does not belong to  this library")  
  
print("***Welcome to Chennai Library***")
print("Library Management system")

books = list(['Python',"Harry porter","C++ Basics","Geronimo stilon","Computer  Visualization"])

L1 = library(books)
while True:
    
    ch = input(("\n1.Add books \n2.Lend books \n3.Return books \n4.Display books \nenter your choice"))
    if ch == "1":
        bookn = input("enter the name")
        L1.addbooks(bookn)
    elif ch == "2":
        bookn = input("enter the name")
        L1.lendbooks(bookn)
    elif ch == "3":
        bookn = input("enter the name")
        L1.returnbooks(bookn)
    elif ch == "4":
        print("display books")
        L1.displaybooks()
    choice = input("enter you want to quit (Y/N)")
    if choice.lower() == 'y':
        break;

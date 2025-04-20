books=[]
def add_book():
    code= input("enter book id: ")
    title=input("enter title of book: ")
    auther=input("enter auther name: ")
    books.append({"code":code,"title":title,"auther":auther})
    
def isavailable():
     codes=input("Enter code of book to be search: ")
     found=any(book["code"] == codes for book in books)
     if found:
             print("book is  available in libary") 
     else:
             print("book is not  available")
        
def issue_book():
    codes=input("enter the code of books in issue: ")
    for book in books:
     if book["code"]==codes:
       books.remove(book)
       print("book is issue in libery")
     return
     print("book is not issue")
        
def return_book():
    add_book()
    print("book return successfully")
        
def delete_book():
    codes=input("enter the book code to be delete: ")
    for book in books:
     if book["code"]==codes:
         books.remove(book) 
         print("book is delete")
    return
    print("book is not delete")
     
        
def main():
    while True:
          print("\n library management system")
          print("1.add_book")
          print("2.isavailable")
          print("3.issue_book")
          print("4.return_book")
          print("5.delete_book")
          print("6.exit")
          choice=input("enter your choice 1-6: ")
          if choice=='1':
            add_book()
            print("book added successfully")
          elif choice=='2':
            isavailable()
          elif choice=='3':
            issue_book()
          elif choice=='4':
            return_book()
          elif choice=='5':
            delete_book()
          elif choice=='6':
            print("exiting")
            break
          else:       
              print("invalid choice, please try again")
              
main()
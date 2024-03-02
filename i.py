class Book:
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre
class Library:
    def __init__(self):
        self.books = []

class LibraryManager(Library, Book):
    def __init__(self):
        super().__init__()
    def addBook(self, book):
        self.books.append(book)
    def removeBook(self, book):
        self.books.remove(book)

    def getList(self):
            for book in self.books:
               print(book.title, book.author, book.genre)
               return self.books
    

class Searcher(Library):
    def __init__(self):
        super().__init__()
    def getList(self):
        for book in self.books:
               print(book.title, book.author, book.genre)

    def searchTitle(self, name):
        for book in self.books:
            if(name == book.title):
                print(name)
            else:
                print("not found")
    def searchAuthor(self, person):
        for book in self.books:
            if(person == book.author):
                print(person)
            else:
                print("not found") 
    def searchGenre(self, type):
        for book in self.books:
            if(type == book.genre):
                print(type)
            else:
                print("not found")  


class StudentInterface(Library):
    def __init__(self):
        self.books = []
    def getList(self):
            for book in self.books:
               print(book.title, book.author, book.genre)
    def searchTitle(self, list, title):
        for book in list:
            if(title == book.title):
                print(title)
            else:
                print("not found")        
    def searchAuthor(self,list, person):
        for book in list:
            if(person == book.author):
                print(person)
            else:
                print("not found")  
        
    def searchGenre(self,list, type):
        for book in list:
            if(type == book.genre):
                print(type)
            else:
                print("not found")  
        

class RegisteredUser(Library):
    def __init__(self):
        self.userbooks = []
    def BorrowBook(self, book):
            self.userbooks.append(book)
            return book
    def ReturnBook(self,book):
        if book in self.userbooks:
            self.userbooks.remove(book)
        return book
    def __str__(self):
        for book in self.userbooks:
            return f"The books you are currently borrowing {book.title} {book.author}  {book.genre}"
    def overdue(self, days):
        if days > 5:
            print("Your fine is $5")
        else:
            print("No charges")

    def rateBook(self, book, rating):
        if book in self.userbooks:
            print(f"The rating of {book.title} is {rating}")
        else: 
            print("you do not have this book")

def main():
    book1 = Book("Fishy", "Dr Seuss", "fiction")

    book2 = Book("Doggy", "Dr Seuss", "nonfiction")

    

    student1 = StudentInterface()
    librarian1 = LibraryManager()
    librarian = Searcher()
    user = RegisteredUser()

    librarian1.addBook(book2)
    librarian1.addBook(book1)

    librarian1.addBook(user.ReturnBook(book1))

    librarian1.removeBook(user.BorrowBook(book1))
    librarian1.getList()

    print(user)
    user.overdue(10)
    user.rateBook(book1, 5)
    student1.searchTitle(librarian1.getList(), "Fishy")
    student1.searchAuthor(librarian1.getList(), "Dr Seuss")
    student1.searchGenre(librarian1.getList(), "nonfiction")
if __name__ == "__main__":
    main()
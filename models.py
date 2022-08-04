class Library:

    def __init__(self,name:str) -> None:
        self.name = name
        self.books = {}
        self.members = {}
        self.librarians = {}
    
    def add_librarian(self,librarian):
        self.librarians[librarian.id] = librarian
    
    def remove_librarian(self, librarian):
        if librarian.id in self.librarians:
            del self.librarians[librarian.id]


class Book:
    def __init__(self,title:str, author:str, publishing_date:str, library:Library, copies_num:int = 1) -> None:
        self.title = title.title()
        self.author = author
        self.publishing_date = publishing_date
        self.copies_num = copies_num
        self.library = library
    
    @property
    def isavailable(self):
        return self.copies_num > 0

    def __str__(self) -> str:
        return f"{self.title}: by {self.author}, publishing_date: {self.publishing_date} .. {self.copies_num} copies"


class Account:
    _accounts_num = 0
    def __init__(self, name:str, email:str) -> None:
        Account._accounts_num += 1
        self._id = Account._accounts_num
        self.name = name
        self.email = email

    @property
    def id(self):
        return self._id

    def __str__(self) -> str:
        return f"(id:{self._id}) {self.name} ... {self.email}"



class Member(Account):
    
    def __init__(self, name: str, email: str) -> None:
        super().__init__(name, email)
        self.borrowed_books = {}

    def borrow(self, book:Book):
        library = book.library
        if self._id in library.members and book.isavailable:
            self.borrowed_books[book.title] = book
            book.copies_num -= 1

    def return_book(self, book:Book):
        library = book.library
        if self._id in library.members and book.title in self.borrowed_books:
            del self.borrowed_books[book.title]
            book.copies_num += 1


class Librarian(Account):

    def add_book(self, book:Book):
        library = book.library
        if self._id in library.librarians:
            if book.title in library.books:
                library.books[book.title].copies_num += book.copies_num
            else:
                library.books[book.title] = book
    
    def remove_book(self, book:Book):
        library = book.library
        if self._id in library.librarians:
            if book.title in library.books:
                del library.books[book.title]
    
    def add_member(self,member:Member, library:Library):
        if self._id in library.librarians:
            library.members[member.id] = member
    
    def remove_member(self,member:Member, library:Library):
        if self._id in library.librarians:
            del library.members[member.id]
        
    
            


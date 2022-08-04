import models
import time

library = models.Library("Knowledge Bank")
librarian = models.Librarian("mohamed","mohamed@gmail.com")
library.add_librarian(librarian)


def main_page():

    print("############### Main Page ##############\n")
    print("1- Display books")
    print("2- Search for a book")
    print("3- Add a book")
    print("4- Remove a book")
    print("5- Members Section")
    print("6- Exit")


def get_key():
    key = int(input("Enter a key: "))
    while not (1<=key<=6):
        key = int(input("Press a key:"))
    
    return key


def display_books():

    print("#"*50)

    for title in library.books:
        print(library.books[title])

    print("#"*50)

def search_for_book():

    title = input("Enter the book title:").title()
    if title in library.books:
        print(library.books[title])
    else:
        print("No results!")


def add_book():
    title = input("Enter the book`s title:").title()
    author = input("Enter the book`s author:")
    publishing_date = input("Enter the book`s publishing_date:")
    copies = int(input("Enter the number of copies:"))
    while copies <= 0:
        copies = int(input("Enter a valid number"))
    new_book = models.Book(title,author,publishing_date,library,copies)
    librarian.add_book(new_book)
    print("Done!")

def remove_book():
    title = input("Enter the book`s title:").title()
    if title not in library.books:
        print("this book does not exist!")
    else:
        book = library.books[title]
        librarian.remove_book(book)
        print("Done!")


def members_section():
    print("############## Members Section #############")
    print("1- Display members")
    print("2- add a member")
    print("3- remove a member")
    print("4- a member needs to borrow a book")
    print("5- a member needs to return a book")
    print("6- back to the main page")



def display_members():

    print("#"*50)

    for id in library.members:
        print(library.members[id])

    print("#"*50)


def add_member():
    name = input("Enter the member`s name:")
    email = input("Enter the member`s email:")
    new_member = models.Member(name,email)
    librarian.add_member(new_member,library)
    print("Done!")


def remove_member():
    id = int(input("Enter the member`s id:"))
    if id not in library.members:
        print("This id does not exist")
    else:
        member = library.members[id]
        librarian.remove_member(member,library)
        print("Done!")


def borrow_book():
    id = int(input("Enter the member`s id:"))
    if id not in library.members:
        print("This id does not exist!!")
    else:
        title = input("Enter the book`s title:").title()
        if title not in library.books:
            print("This book does not exist!!")
        elif not library.books[title].isavailable:
            print("This book is not available now")
        else:
            member = library.members[id]
            book = library.books[title]
            member.borrow(book)
            print("Done!")


def return_book():
    id = int(input("Enter the member`s id:"))
    if id not in library.members:
        print("This id does not exist!!")
    else:
        member = library.members[id]
        title = input("Enter the book`s title:").title()
        if title not in member.borrowed_books:
            print("This book has not been borrowed by this member.")
        else:
            book = member.borrowed_books[title]
            member.return_book(book)
            print("Done!")
def app():

    main_page()
    key = get_key()

    while True:

        if key == 6:
            print("Exiting...")
            return False
        elif key == 1:
            display_books()
        elif key == 2:
            search_for_book()
        elif key == 3:
            add_book()
        elif key == 4:
            remove_book()

        while key == 5:
            members_section()
            k = get_key()

            if k == 1:
                display_members()
            elif k == 2:
                add_member()
            elif k == 3:
                remove_member()
            elif k == 4:
                borrow_book()
            elif k == 5:
                return_book()
            elif k == 6:
                break
            time.sleep(1)
        
        time.sleep(1)
        main_page()
        key = get_key()
        

app()


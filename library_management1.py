# Global list of students
list_std = ["John Smith", "Jane Johnson", "Jay Bhogal", "Mike Wong"]

# Data structure for library management system using dictionary
datastore = {
    "library": {
        "books": [
            {"title": "Book Title 1", "author": "Author 1", "isbn": "1234567890123", "status": "available"},
            {"title": "Book Title 2", "author": "Author 2", "isbn": "1234567890124", "status": "available"}
        ]
    }
}


# Function to create a new book
def create_book(title, author, isbn):
    return {"title": title, "author": author, "isbn": isbn, "status": "available"}


# Function to add a book to the database
def add_book_to_database(book):
    datastore["library"]["books"].append(book)


# Function to find a book in the database by ISBN
def find_book_in_database(isbn):
    for book in datastore["library"]["books"]:
        if book['isbn'] == isbn:
            return book
    return None


# Function to update the status of a book
def update_book_status(isbn, status):
    book = find_book_in_database(isbn)
    if book:
        book['status'] = status


# Function to add a book
def add_book(title, author, isbn):
    if not title or not author or not isbn:
        print("Error: All fields must be filled")
        return "Failure"

    if len(isbn) != 13:
        print("Error: Invalid ISBN")
        return "Failure"

    book = create_book(title, author, isbn)
    add_book_to_database(book)
    print("Book added successfully")
    return "Success"


# Function to search for books
def search_books(criteria):
    results = []
    for book in datastore["library"]["books"]:
        if (criteria['title'] in book['title']) or (criteria['author'] in book['author']):
            results.append(book)

    if not results:
        print("No results found")
        return "No results found"
    else:
        print("Search results:", results)
        return results


# Function to check book in/out
def check_book_in_out(user_id, book_id, action):
    book = find_book_in_database(book_id)
    if not book:
        print("Error: Book not found")
        return "Failure"

    if book['status'] == "checked out" and action == "checkout":
        print("Error: Book already checked out")
        return "Failure"
    elif book['status'] == "available" and action == "return":
        print("Error: Book not checked out")
        return "Failure"
    elif book['status'] == "available" and action == "checkout":
        update_book_status(book_id, "checked out")
        print("Book checked out successfully")
        return "Success"
    elif book['status'] == "checked out" and action == "return":
        update_book_status(book_id, "available")
        print("Book returned successfully")
        return "Success"
    else:
        print("Error: Invalid action")
        return "Failure"


def manage_library():
    print(""" 

  ------------------------------------------------------
 |======================================================| 
 |======== Welcome To Library Management System ========|
 |======================================================|
  ------------------------------------------------------

Enter 1 : To View Book List 
Enter 2 : To Add New Book 
Enter 3 : To Search Book 
Enter 4 : To Check Out a Book 
Enter 5 : To Return a Book

        """)

    try:
        user_input = int(input("Please select an option: "))
    except ValueError:
        exit("\nHy! That's Not A Number")
    else:
        print("\n")

    if user_input == 1:
        print("List of Books\n")
        for book in datastore["library"]["books"]:
            print("=> Title: {}, Author: {}, ISBN: {}, Status: {}".format(
                book['title'], book['author'], book['isbn'], book['status']))

    elif user_input == 2:
        title = input("Enter Book Title: ")
        author = input("Enter Book Author: ")
        isbn = input("Enter Book ISBN: ")
        add_book(title, author, isbn)

    elif user_input == 3:
        criteria = {"title": input("Enter Title (leave blank if not applicable): "),
                    "author": input("Enter Author (leave blank if not applicable): ")}
        search_books(criteria)

    elif user_input == 4:
        user_id = input("Enter Your Name: ")
        if user_id not in list_std:
            print("Error: User not found")
            return
        book_id = input("Enter Book ISBN: ")
        check_book_in_out(user_id, book_id, "checkout")

    elif user_input == 5:
        user_id = input("Enter Your Name: ")
        if user_id not in list_std:
            print("Error: User not found")
            return
        book_id = input("Enter Book ISBN: ")
        check_book_in_out(user_id, book_id, "return")

    elif user_input < 1 or user_input > 5:
        print("Please Enter Valid Option")


def manage_student():
    print(""" 

  ------------------------------------------------------
 |======================================================| 
 |======== Welcome To Student Management System ========|
 |======================================================|
  ------------------------------------------------------

Enter 1 : To View Student's List 
Enter 2 : To Add New Student 
Enter 3 : To Search Student 
Enter 4 : To Remove Student 

        """)

    try:
        user_input = int(input("Please select an option: "))
    except ValueError:
        exit("\nHy! That's Not A Number")
    else:
        print("\n")

    if user_input == 1:
        print("List Students\n")
        for students in list_std:
            print("=> {}".format(students))

    elif user_input == 2:
        new_std = input("Enter New Student: ")
        if new_std in list_std:
            print("\nThis Student {} Already In The Database".format(new_std))  # Error Message
        else:
            list_std.append(new_std)
            print("\n=> New Student {} Successfully Add \n".format(new_std))
            for students in list_std:
                print("=> {}".format(students))

    elif user_input == 3:
        src_std = input("Enter Student Name To Search: ")
        if src_std in list_std:
            print("\n=> Record Found Of Student {}".format(src_std))
        else:
            print("\n=> No Record Found Of Student {}".format(src_std))  # Error Message

    elif user_input == 4:
        rm_std = input("Enter Student Name To Remove: ")
        if rm_std in list_std:
            list_std.remove(rm_std)
            print("\n=> Student {} Successfully Deleted \n".format(rm_std))
            for students in list_std:
                print("=> {}".format(students))
        else:
            print("\n=> No Record Found of This Student {}".format(rm_std))  # Error Message

    elif user_input < 1 or user_input > 4:
        print("Please Enter Valid Option")


def main_menu():
    while True:
        print(""" 

      ------------------------------------------------------
     |======================================================| 
     |======== Welcome To Management System	========|
     |======================================================|
      ------------------------------------------------------

    Enter 1 : To Manage Library 
    Enter 2 : To Manage Students 
    Enter 3 : To Exit 

            """)

        try:
            user_input = int(input("Please select an option: "))
        except ValueError:
            print("\nHy! That's Not A Number")
            continue
        else:
            print("\n")

        if user_input == 1:
            manage_library()
        elif user_input == 2:
            manage_student()
        elif user_input == 3:
            quit()
        else:
            print("Please Enter Valid Option")


main_menu()
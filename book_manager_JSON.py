import os
import time
import json

BOOKS_FILE = 'books.json'

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def load_books():
    """
    Loads books from the JSON file.
    """
    if os.path.exists(BOOKS_FILE) and os.path.getsize(BOOKS_FILE) > 0:
        with open(BOOKS_FILE, 'r') as f:
            return json.load(f)
    return []

def save_books(books):
    """
    Saves books to the JSON file.
    """
    with open(BOOKS_FILE, 'w') as f:
        json.dump(books, f, indent=4)
        
class Books:
    def __init__(self, title, author, id, status):
        self.title = title
        self.author = author
        self.id = id
        self.status = status
    
    def display(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"ID: {self.id}")
        print(f"Status: {self.status}")

    @staticmethod
    def change_status(book_list):
        while True:
            inp_change = input("Enter The New Status: ")
            if inp_change in ["active", "inactive"]:
                IDD = input("Enter The ID Of Book: ")
                found = False
                for book in book_list:
                    if book['id'] == IDD:
                        book['status'] = inp_change
                        found = True
                        print("The book status is changed successfully.")
                        break
                if not found:
                    print(f"This ID {IDD} is Not Found.")
                break
            else:
                print("Enter 'active' Or 'inactive' please.")
        time.sleep(1)


def create_book():
    title = input("Enter The Title of Book: ")
    clear()
    author = input("Enter The author of Book: ")
    clear()
    while True:
        id_input = input("Enter The ID: ")
        if id_input.isdigit():
            # Check for unique ID
            books = load_books()
            if any(book['id'] == id_input for book in books):
                print("This ID already exists. Please enter a different ID.")
                time.sleep(1)
            else:
                break
        else:
            print("Enter A Number.")
            time.sleep(1)
    clear()
    while True:
        status = input("Enter The Status Of Book (Press Enter To Skip): ").lower()
        if not status or status in ["active", "inactive"]:
            if not status:
                status = "inactive"
            break
        else:
            print("Please enter 'active' or 'inactive'.")
    print("The Book Is Added.....")
    time.sleep(1)
    clear()
    return {"title": title, "author": author, "id": id_input, "status": status}

def search_book(book_list):
    print("1-Search by Title.\n2-Search by ID.\n3-Search by status.\n4-BACK_Menu.")
    choice2 = input("Enter Your choice: ")
    found_books = []

    if choice2 == "1":
        tl = input("Enter The Title Of The Book: ")
        found_books = [b for b in book_list if b['title'].lower() == tl.lower()]
    elif choice2 == "2":
        IDD = input("Enter The ID For Book: ")
        found_books = [b for b in book_list if b['id'] == IDD]
    elif choice2 == "3":
        stat = input("Enter The Status Of The Book: ")
        found_books = [b for b in book_list if b['status'].lower() == stat.lower()]
    elif choice2 == "4":
        print("Exiting search...")
        time.sleep(1)
        return
    else:
        print("Invalid Choice.")
        time.sleep(1)
        return

    clear()
    if not found_books:
        print("No books found matching your search.")
    else:
        for book in found_books:
            print("-" * 20)
            print(f"Title: {book['title']}")
            print(f"Author: {book['author']}")
            print(f"ID: {book['id']}")
            print(f"Status: {book['status']}")
            print("-" * 20)
    time.sleep(5)

def show_books(book_list):
    clear()
    if not book_list:
        print("The Library is empty.")
    else:
        for book in book_list:
            print("-" * 20)
            print(f"Title: {book['title']}")
            print(f"Author: {book['author']}")
            print(f"ID: {book['id']}")
            print(f"Status: {book['status']}")
            print("-" * 20)
    time.sleep(5)

def main():
    while True:
        clear()
        print("1-Add New Book.\n2-Show All Books.\n3-Search In Books.\n4-Change Status.\n5-Exit.")
        choice = input("Enter Your choice: ")
        
        books_data = load_books()
        
        if choice == "1":
            new_book = create_book()
            books_data.append(new_book)
            save_books(books_data)
        elif choice == "2":
            show_books(books_data)
        elif choice == "3":
            search_book(books_data)
        elif choice == "4":
            Books.change_status(books_data)
            save_books(books_data)
        elif choice == "5":
            print("Exiting...")
            time.sleep(2)
            break
        else:
            print("Invalid Input.")
            time.sleep(1)

if __name__ == "__main__":
    main()
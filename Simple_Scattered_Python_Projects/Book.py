import os

# Define constants
BOOKS_FILE = "books.txt"

# Define functions
def display_menu():
    """Display the Bookshop menu"""
    print(" Bookshop Application")
    print("[1] Add a book")
    print("[2] Update copies of a book")
    print("[3] Delete a book")
    print("[4] Display all books")
    print("[5] Display details of a book")
    print("[6] Display books by a given publisher")
    print("[7] Display books in a given series title")
    print("[8] Display books by a given author")
    print("[9] Display the value of all books")
    print("[0] Exit")

def get_books():
    """Read the books.txt file and return a list of dictionaries"""
    books = []
    if os.path.exists(BOOKS_FILE):
        with open(BOOKS_FILE, "r") as f:
            for line in f:
                values = line.strip().split(",")
                book = {
                    "title": values[0],
                    "authors": values[1].split(";"),
                    "series_title": values[2],
                    "copies": int(values[3]),
                    "year": int(values[4]),
                    "publisher": values[5],
                    "price": float(values[6])
                }
                books.append(book)
    return books

def add_book(books):
    """Add a new book to the list"""
    print("Bookshop Application – Add a book:")
    print("=" * 35)
    title = input("Enter the title: ")
    authors = input("Enter author(s) delimited by a comma: ").split(",")
    series_title = input("Enter series title: ")
    copies = int(input("Enter number of copies: "))
    year = int(input("Enter year: "))
    publisher = input("Enter publisher name: ")
    price = float(input("Enter the price: "))
    # Generate the BS_Code for the new book
    last_book = books[-1]
    last_code = int(last_book["BS_Code"][2:])
    new_code = f"QA{last_code + 1:05d}"
    # Create the new book dictionary
    new_book = {"BS_Code": new_code, "title": title, "authors": authors, "series_title": series_title, 
                "copies": copies, "year": year, "publisher": publisher, "price": price}
    # Append the new book to the list
    books.append(new_book)
    # Save the updated list to the file
    with open("books.txt", "a") as file:
        file.write(f"{new_code};{title};{','.join(authors)};{series_title};{copies};{year};{publisher};{price}\n")
    print(f"Record added: {new_code} - {title} by {', '.join(authors)}")

def delete_book(books):
    """Delete a book from the list"""
    print("Bookshop Application – Delete a book:")
    print("=" * 35)
    code = input("Enter the BS_Code of the book to delete: ")
    # Find the book with the specified code
    for book in books:
        if book["BS_Code"] == code:
            # Remove the book from the list
            books.remove(book)
            # Save the updated list to the file
            with open("books.txt", "w") as file:
                for book in books:
                    file.write(f"{book['BS_Code']};{book['title']};{','.join(book['authors'])};{book['series_title']};{book['copies']};{book['year']};{book['publisher']};{book['price']}\n")
            print(f"Record deleted: {code} - {book['title']} by {', '.join(book['authors'])}")
            return
    # If the book with the specified code is not found
    print(f"Book not found: {code}")

def delete_book(books):
    """Delete a book from the list"""
    print("Bookshop Application – Delete a book:")
    print("=" * 35)
    code = input("Enter the BS_Code of the book to delete: ")
    # Find the book with the specified code
    for book in books:
        if book["BS_Code"] == code:
            # Remove the book from the list
            books.remove(book)
            # Save the updated list to the file
            with open("books.txt", "w") as file:
                for book in books:
                    file.write(f"{book['BS_Code']};{book['title']};{','.join(book['authors'])};{book['series_title']};{book['copies']};{book['year']};{book['publisher']};{book['price']}\n")
            print(f"Record deleted: {code} - {book['title']} by {', '.join(book['authors'])}")

def update_book(books):
    """Update the number of copies of a book"""
    print("Bookshop Application – Update copies of a book:")
    print("=" * 35)
    code = input("Enter the BS_Code of the book to update: ")
    # Find the book with the specified code
    for book in books:
        if book["BS_Code"] == code:
            old_copies = book["copies"]
            new_copies = int(input(f"Enter the new number of copies for {book['title']} by {', '.join(book['authors'])}: "))
            if new_copies < 0 and abs(new_copies) > old_copies:
                print(f"Cannot remove {abs(new_copies)} copies. Only {old_copies} copies available.")
            else:
                book["copies"] = old_copies + new_copies
                # Save the updated list to the file
                with open("books.txt", "w") as file:
                    for book in books:
                        file.write(f"{book['BS_Code']};{book['title']};{','.join(book['authors'])};{book['series_title']};{book['copies']};{book['year']};{book['publisher']};{book['price']}\n")
                print(f"{new_copies} copies of {book['title']} by {', '.join(book['authors'])} added. Total copies: {book['copies']}")
		   
                    	




def display_books(books):
    """Display all books in the list"""
    print("Bookshop Application – Display all books:")
    print("=" * 35)
    for book in books:
        print(f"{book['title']} by {', '.join(book['authors'])}")
        print(f"Copies: {book['copies']}")
        print(f"Year: {book['year']}")
        print(f"Publisher: {book['publisher']}")
        print(f"Series Title: {book['series_title']}")
        print(f"Price: {book['price']} QR")
        print("=" * 35)

def display_book_details(books):
    """Display details of a particular book"""
    title = input("Enter the title of the book: ")
    found = False
    for book in books:
        if book["title"].lower() == title.lower():
            print("=" * 35)
            print(f"Title: {book['title']}")
            print(f"Author(s): {', '.join(book['authors'])}")
            print(f"Copies: {book['copies']}")
            print(f"Year: {book['year']}")
            print(f"Publisher: {book['publisher']}")
            print(f"Series Title: {book['series_title']}")
            print(f"Price: {book['price']} QR")
            print("=" * 35)
            found = True
            break
    if not found:
        print(f"{title} is not in the list.")

def display_books_by_publisher(books):
    """Display books by a given publisher"""
    publisher = input("Enter the name of the publisher: ")
    found = False
    print("=" * 35)
    for book in books:
        if book["publisher"].lower() == publisher.lower():
            print(f"{book['title']} by {', '.join(book['authors'])}")
            found = True
    if not found:
        print(f"No books by {publisher}.")

def display_books_by_series_title(books):
    """Display books in a given series title"""
    series_title = input("Enter the series title: ")
    found = False
    print("=" * 35)
    for book in books:
        if book["series_title"].lower() == series_title.lower():
            print(f"{book['title']} by {', '.join(book['authors'])}")
            found = True
    if not found:
        print(f"No books in the series {series_title}.")

def display_books_by_author(books):
    """Display books by a given author"""
    author = input("Enter the name of the author: ")
    found = False
    print("=" * 35)
    for book in books:
        if author.lower() in [x.lower() for x in book["authors"]]:
            print(f"{book['title']} by {', '.join(book['authors'])}")
            found = True
    if not found:
        print(f"No books by {author}.")

def display_books_value(books):
    """Display the total value of all books"""
    total_value = 0
    for book in books:
        total_value += book['price'] * book['copies']
    print(f"Total value of all books: {total_value} QR")

def main():
    books = get_books()
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            add_book(books)
        elif choice == "2":
            update_book(books)
        elif choice == "3":
            delete_book(books)
        elif choice == "4":
            display_books(books)
        elif choice == "5":
            display_book_details(books)
        elif choice == "6":
            display_books_by_publisher(books)
        elif choice == "7":
            display_books_by_series_title(books)
        elif choice == "8":
            display_books_by_author(books)
        elif choice == "9":
            display_books_value(books)
        elif choice == "0":
            save_books(books)
            print("Exiting the Bookshop Application...")
            break
        else:
            print("Invalid choice. Please try again.\n")
    
if __name__ == '__main__':
    main()


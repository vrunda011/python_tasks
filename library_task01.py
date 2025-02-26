def add_book(title, author, quantity):
    if title in books:
        books[title]['quantity'] += quantity
    else:
        books[title] = {'author': author, 'quantity': quantity}

def remove_book(title):
    if title in books:
        del books[title]
        print(f'"{title}" removed successfully.')
    else:
        print(f'"{title}" not found in the library.')

def update_info(title, new_author, new_quantity):
    if title in books:
        books[title]['author'] = new_author
        books[title]['quantity'] = new_quantity
        print(f'"{title}" updated successfully.')
    else:
        print(f'"{title}" not found in the library.')

def display_books():
    if books:
        print("\nLibrary Inventory:")
        for title, info in books.items():
            print(f'Title: {title}, Author: {info.get("author")}, Quantity: {info.get("quantity")}')
    else:
        print("\nNo books in the inventory.")

def search_book(title):
    if title in books:
        print(f'\nTitle: {title}, Author: {books[title]["author"]}, Quantity: {books[title]["quantity"]}')
    else:
        print(f'"{title}" not found in the library.')

books = {}

while True:
    print("\nLibrary Inventory Management System")
    print("1. Add Book")
    print("2. Remove Book")
    print("3. Update Book")
    print("4. Display Books")
    print("5. Search Book")
    print("6. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        title = input("Enter title: ")
        author = input("Enter author: ")
        quantity = int(input("Enter quantity: "))
        add_book(title, author, quantity)

    elif choice == '2':
        title = input("Enter title: ")
        remove_book(title)

    elif choice == '3':
        title = input("\nEnter title of book to update: ")
        new_author = input("Enter new author: ")
        new_quantity = int(input("Enter new quantity: "))
        update_info(title, new_author, new_quantity)

    elif choice == '4':
        display_books()

    elif choice == '5':
        title = input("Enter title to search: ")
        search_book(title)

    elif choice == '6':
        print("Thank you for using this library.")
        break

    else:
        print("Invalid choice.")

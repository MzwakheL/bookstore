import sqlite3

# Create the books table if it doesn't exist
def create_table():
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY,
            title TEXT,
            author TEXT,
            qty INTEGER
        )
    ''')
# Poluating the information given to the table
def populate_table():
    books = [
        (3001, "A Tale of Two Cities", "Charles Dickens", 30),
        (3002, "Harry Potter and the Philosopher's Stone", "J.K. Rowling", 40),
        (3003, "The Lion, the Witch and the Wardrobe", "C.S. Lewis", 25),
        (3004, "The Lord of the Rings", "J.R.R. Tolkien", 37),
        (3005, "Alice in Wonderland", "Lewis Carroll", 12)
    ]
    cursor.executemany("INSERT INTO books VALUES (?, ?, ?, ?)", books)
    db.commit()

# Define a function to enter a new book
def add_book():
    title = input("Enter title: ")
    author = input("Enter author: ")
    qty = int(input("Enter quantity: "))
    cursor.execute("INSERT INTO books (title, author, qty) VALUES (?, ?, ?)", (title, author, qty))
    db.commit()
    print("Book added successfully.")

# Define a function to update an existing book
def update_book():
    book_id = int(input("Enter book ID: "))
    new_title = input("Enter new title (press Enter to keep current): ")
    new_author = input("Enter new author (press Enter to keep current): ")
    new_qty = input("Enter new quantity (press Enter to keep current): ")
    updates = {}
    if new_title:
        updates["title"] = new_title
    if new_author:
        updates["author"] = new_author
    if new_qty:
        updates["qty"] = new_qty
    if not updates:
        print("No updates were made.")
        return
    set_clause = ", ".join([f"{k} = ?" for k in updates.keys()])
    values = tuple(updates.values()) + (book_id,)
    cursor.execute(f"UPDATE books SET {set_clause} WHERE id = ?", values)
    db.commit()
    print("Book updated successfully.")

# Define a function to delete an existing book
def delete_book():
    book_id = int(input("Enter book ID: "))
    cursor.execute("DELETE FROM books WHERE id = ?", (book_id,))
    db.commit()
    print("Book deleted successfully.")

# Define a function to search for a book (Author name or title)
def search_books():
    search_term = input("Enter search term: ")
    cursor.execute("SELECT * FROM books WHERE title LIKE ? OR author LIKE ?", ('%' + search_term + '%', '%' + search_term + '%'))
    books = cursor.fetchall()
    if not books:
        print("No books found.")
    else:
        print(f"Found {len(books)} books:")
        for book in books:
            print(f"ID: {book[0]}, Title: {book[1]}, Author: {book[2]}, Qty: {book[3]}")

db = sqlite3.connect('ebookstore.db')
cursor = db.cursor()

create_table()
populate_table()

# Display the menu and get user input
while True:
    print("\nMenu:")
    print("1. Enter book")
    print("2. Update book")
    print("3. Delete book")
    print("4. Search books")
    print("0. Exit")

# Take actions based on user input
    choice = input("Enter your choice: ")
    if choice == '1':
        add_book()
    elif choice == '2':
        update_book()
    elif choice == '3':
        delete_book()
    elif choice == '4':
        search_books()
    elif choice == '0':
        break
    else:
        print("Invalid choice. Please try again")


# reference - https://www.tutorialspoint.com/python_data_access/python_sqlite_create_table.htm
# reference - https://stackoverflow.com/questions/18244565/how-can-i-use-executemany-to-insert-into-mysql-a-list-of-dictionaries-in-python
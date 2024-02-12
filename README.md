# bookstore


# Description
The Python SQLite Bookstore Management System is a command-line application designed to manage a bookstore's inventory. It utilizes SQLite for database management, allowing users to perform various operations such as adding new books, updating existing books, deleting books, and searching for books based on title or author. The system provides an efficient and user-friendly interface for managing bookstore inventory data.

# Features
Database Creation: Automatically creates a SQLite database and the necessary table (books) if they don't exist.
Data Population: Populates the books table with sample book entries upon database creation.
Book Addition: Allows users to add new book entries to the database, providing details such as title, author, and quantity.
Book Update: Enables users to update existing book entries, including modifications to title, author, and quantity.
Book Deletion: Provides functionality to delete existing book entries from the database based on book ID.
Book Search: Allows users to search for books based on title or author, providing a list of matching books.

# Usage
Installation: Clone the repository or download the Python script (bookstore.py) to your local machine.
Dependencies: Ensure you have Python installed on your system, along with the sqlite3 module (which is included in Python's standard library).
Run the Script: Open a terminal or command prompt, navigate to the directory containing the script, and run the script using the command python bookstore.py.
Main Menu: Upon running the script, users will be presented with a main menu where they can select various options to manage bookstore inventory.
Input: Follow the on-screen instructions to perform desired operations such as adding books, updating book details, deleting books, and searching for books.
Output: The script will display relevant information based on user input, providing feedback on the success of operations and presenting search results.

# Example Usage
Adding a Book:

mathematica
Copy code
Menu:
1. Enter book
2. Update book
3. Delete book
4. Search books
0. Exit

Enter your choice: 1

Enter title: The Great Gatsby
Enter author: F. Scott Fitzgerald
Enter quantity: 20

Book added successfully.
Searching for Books:

yaml
Copy code
Menu:
1. Enter book
2. Update book
3. Delete book
4. Search books
0. Exit

Enter your choice: 4

Enter search term: Potter

Found 1 books:
ID: 3002, Title: Harry Potter and the Philosopher's Stone, Author: J.K. Rowl

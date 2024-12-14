# Book class to store information about a single book
class Book:
    def __init__(self, title, author, year, isbn, pages):
        """Initialize a new Book instance with title, author, year, ISBN, and number of pages.""" 
        self.title = title
        self.author = author
        self.year = year
        self.isbn = isbn
        self.pages = pages

    def __str__(self):
        """Return a string representation of the book details."""
        return f"Title: {self.title}, Author: {self.author}, Year: {self.year}, ISBN: {self.isbn}, Pages: {self.pages}"


# Library class to manage a collection of Book objects
class Library:
    def __init__(self):
        """Initialize an empty list to store the collection of books."""
        self.books = []

    def add_book(self, title, author, year, isbn, pages):
        """Create a new Book object and add it to the collection."""
        new_book = Book(title, author, year, isbn, pages)
        self.books.append(new_book)
        print(f"\nBook '{title}' added successfully!\n")

    def display_books(self):
        """Display all the books in the collection."""
        if not self.books:
            print("\nThe library is currently empty.\n")
        else:
            print("\nLibrary Collection:")
            for idx, book in enumerate(self.books, start=1):
                print(f"{idx}. {book}")
            print("\n")

    def search_books_by_title(self, title):
        """Search for books by title."""
        found_books = [book for book in self.books if title.lower() in book.title.lower()]
        if not found_books:
            print(f"\nNo books found with title containing '{title}'.\n")
        else:
            print(f"\nBooks matching '{title}':")
            for idx, book in enumerate(found_books, start=1):
                print(f"{idx}. {book}")
            print("\n")


def main():
    """Main function to run the library system."""
    library = Library()
    
    while True:
        print("Library Management System")
        print("1. Add a new book")
        print("2. View all books")
        print("3. Search for a book by title")
        print("4. Exit")
        
        try:
            choice = int(input("\nEnter your choice (1-4): "))
        except ValueError:
            print("\nInvalid input. Please enter a number between 1 and 4.\n")
            continue
        
        if choice == 1:
            title = input("\nEnter the book title: ")
            author = input("Enter the author's name: ")
            try:
                year = int(input("Enter the year of publication: "))
                pages = int(input("Enter the number of pages: "))
            except ValueError:
                print("\nYear and pages must be integers.\n")
                continue
            isbn = input("Enter the ISBN number: ")
            
            library.add_book(title, author, year, isbn, pages)
        
        elif choice == 2:
            library.display_books()
        
        elif choice == 3:
            title = input("\nEnter the title (or part of it) to search for: ")
            library.search_books_by_title(title)
        
        elif choice == 4:
            print("\nExiting the Library Management System. Goodbye!\n")
            break
        
        else:
            print("\nInvalid choice. Please enter a number between 1 and 4.\n")


if __name__ == "__main__":
    main()

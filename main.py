import json
from library import librarian


FILE_NAME = "books.json"


def load_books():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)

    except FileNotFoundError:
        return {}


def save_books(library):
    with open(FILE_NAME, "w") as file:
        json.dump(library, file, indent=4)


def search_books(library):

    search = input("Enter book title, author, or ISBN: ").lower()

    found = False

    for book in library.values():

        if (
            search in book["title"].lower()
            or search in book["author"].lower()
            or search in book["isbn"]
        ):

            if book["available"]:
                status = "Available"
            else:
                status = "Checked Out"

            print(
                f'{book["title"]} by {book["author"]} '
                f'(ISBN: {book["isbn"]}) - {status}'
            )

            found = True

    if not found:
        print("No books found.")


def main():

    library = load_books()

    while True:

        print("\n===== Library Management System =====")

        print("1. Add Book")
        print("2. Display All Books")
        print("3. Search Books")
        print("4. Delete Book")
        print("5. Borrow Book")
        print("6. Return Book")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":

            title = input("Enter book title: ")
            author = input("Enter author: ")
            isbn = input("Enter ISBN: ")

            librarian.add_book(library, title, author, isbn)

            save_books(library)

        elif choice == "2":

            librarian.display_books(library)

        elif choice == "3":

            search_books(library)

        elif choice == "4":

            isbn = input("Enter ISBN: ")

            librarian.remove_book(library, isbn)

            save_books(library)

        elif choice == "5":

            isbn = input("Enter ISBN: ")

            librarian.check_out_book(library, isbn)

            save_books(library)

        elif choice == "6":

            isbn = input("Enter ISBN: ")

            librarian.return_book(library, isbn)

            save_books(library)

        elif choice == "7":

            print("Thank you for using the Library Management System.")
            break

        else:

            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
def add_book(library, title, author, isbn):

    if isbn in library:
        print("Book with this ISBN already exists.")
        return

    library[isbn] = {
        "title": title,
        "author": author,
        "isbn": isbn,
        "available": True
    }

    print("Book added successfully.")


def remove_book(library, isbn):

    if isbn not in library:
        print("Book not found.")
        return

    del library[isbn]

    print("Book removed successfully.")


def check_out_book(library, isbn):

    if isbn not in library:
        print("Book not found.")
        return

    if not library[isbn]["available"]:
        print("Book is already checked out.")
        return

    library[isbn]["available"] = False

    print("Book checked out successfully.")


def return_book(library, isbn):

    if isbn not in library:
        print("Book not found.")
        return

    library[isbn]["available"] = True

    print("Book returned successfully.")


def display_books(library):

    if not library:
        print("No books found.")
        return

    for isbn, book in library.items():

        if book["available"]:
            status = "Available"
        else:
            status = "Checked Out"

        print(
            f'{book["title"]} by {book["author"]} '
            f'(ISBN: {book["isbn"]}) - {status}'
        )
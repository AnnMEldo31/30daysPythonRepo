from helper_functions import insert_book, get_all_books, mark_book_as_read, delete_book

def prompt_add_book():
    name = input('Enter the new book name: ')
    author = input('Enter the new book author: ')

    insert_book(name, author)


def list_books():
    for book in get_all_books():
        read = 'YES' if book['read'] == '1' else 'NO'  # book[3] will be a falsy value (0) if not read
        print(f"{book['name']} by {book['author']} — Read: {read}")


def prompt_read_book():
    name = input('Enter the name of the book you just finished reading: ')

    mark_book_as_read(name)


def prompt_delete_book():
    name = input('Enter the name of the book you wish to delete: ')

    delete_book(name)
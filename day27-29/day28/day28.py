from typing import List, Dict, Any, Callable

Book = Dict[str, str]
BookList = List[Book]
Operation = Callable[[BookList, Book], Any]


def get_books() -> BookList:
    # new empty list
    reading_list: BookList = []

    # read from file into list
    with open("books2.csv", "r") as f:
        rows: List[str] = f.readlines()

    # extract header values
    headers: List[str] = rows[0].strip().split(",")

    # extract actual data into dicts, appended to list
    for row in rows[1:]:
        reading_list.append(dict(zip(headers, row.strip().split(","))))

    # return list
    return reading_list


def list_books(reading_list: BookList):
    print()

    # get unit from list
    for book in reading_list:
        # get values from unit
        title, author, year, read = book.values()

        # print formatted string
        print(f"{title} ({year}) by {author} - {read}")


def find_books() -> BookList:
    # new empty list
    matching_books: BookList = []

    # user input
    search_term: str = input("Enter the title or part of the title: ").strip().lower()

    # get books
    book_list: BookList = get_books()

    # search for term in each title
    for book in book_list:
        if search_term in book['title'].lower():
            # result found, append to list
            matching_books.append(book)

    # return list
    return matching_books


def add_book():
    # take user inputs
    title: str = input("Enter the book's title : ").strip()
    author: str = input("Enter the author's name: ").strip()
    year: str = input("Enter the year of publication: ").strip()

    # create formatted string and append string to file
    with open("books2.csv", "a") as f:
        f.write(f"{title},{author},{year},Not Read\n")

    # line break
    print(f"\n{title} ({year}) by {author} - Not Read\n")


def print_reading_list():
    # get books
    reading_list: BookList = get_books()

    # list the books
    if reading_list:
        list_books(reading_list)
    else:
        print("\nNo books in the reading list\n")


def search_books():
    # find books
    found_books: BookList = find_books()

    # print
    if found_books:
        list_books(found_books)
    else:
        print("No books found")


def mark_read(reading_list: BookList, book: Book):
    mod_index: int = reading_list.index(book)

    if reading_list[mod_index]['read'] == "Not Read":
        reading_list[mod_index]['read']: str = "Read"
        print(f"{book['title']} marked Read\n")
    else:
        print(f"{book['title']} already read\n")


def delete_book(reading_list: BookList, book: Book):
    title: str = book['title']
    reading_list.remove(book)
    print(f"{title} removed")


def modify_reading_list(operation: Operation):
    # get books
    reading_list: BookList = get_books()

    # search for term in each title
    found_books: BookList = find_books()

    # 1st result found, operation performed
    if found_books:
        operation(reading_list, found_books[0])

        # write back to file
        with open("books2.csv", "w") as f:
            f.write("title,author,year,read\n")
            for book in reading_list:
                f.write(",".join(book.values()) + "\n")

    # if result not found
    else:
        print("No book found")


user_prompt: str = '''\nPlease enter one of the following options:

- 'a' to add a book
- 'l' to list the books
- 's' to search for book(s) by title
- 'r' to mark a book (searched by title) as read
- 'd' to delete a book (searched by title)
- 'q' to quit

What would you like to do? '''

while True:
    user_input: str = input(user_prompt).strip().lower()

    if user_input == 'a':
        add_book()

    elif user_input == 'l':
        print_reading_list()

    elif user_input == 's':
        search_books()

    elif user_input == 'r':
        modify_reading_list(mark_read)

    elif user_input == 'd':
        modify_reading_list(delete_book)

    elif user_input == 'q':
        print("Quit")
        break

    else:
        print("Invalid input")

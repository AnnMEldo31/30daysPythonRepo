# Users should be able to add a book to their reading list by providing a book title, an author's name, a year of publication, and whether or not the book has been read.
# The program should store information about all of these books in a file called books2.csv, and this data should be stored in CSV format.
# Users should be able to retrieve the books in their reading list, and these books should be printed out in a user-friendly format.
# Users should be able to search for a specific book by providing a book title.
# Users should be able to mark a book as read by entering a book title. If there are multiple books with the same title, you can just mark the first matching book as read.
# Users should be able to delete books from their reading list by providing the book title for the book they want to delete. Once again, you can just delete the first matching book.
# Users should be able to select these options from a text menu, and they should be able to perform multiple operations without restarting the program. You can see an example of a working menu in the post on while loops (day 8).

# Day 14 Project: Reading List (Hard Version)

def get_books() :
  # new empty list
  reading_list = []
  
  # read from file into list
  with open("books2.csv", "r") as f:
    rows = f.readlines()

  # extract header values
  headers = rows[0].strip().split(",")

  # extract actual data into dicts, appended to list
  for row in rows[1:] :
    reading_list.append(dict(zip(headers, row.strip().split(","))))

  # return list
  return reading_list


def list_books(reading_list) :
  print()

  # get unit from list
  for book in reading_list:
    # get values from unit
    title, author, year, read = book.values()
    
    # print formatted string
    print(f"{title} ({year}) by {author} - {read}")  


def find_books() :
  # new empty list
  matching_books = []
  
  # user input
  search_term = input("Enter the title or part of the title: ").strip().lower()

  # get books
  book_list = get_books()
  
  # search for term in each title
  for book in book_list :
    if search_term in book['title'].lower() :
      # result found, append to list
      matching_books.append(book)

  # return list
  return matching_books


def add_book() :
  # take user inputs
  title = input("Enter the book's title : ").strip()
  author = input("Enter the author's name: ").strip()
  year = input("Enter the year of publication: ").strip()

  # create formatted string and append string to file
  with open("books2.csv", "a") as f:
    f.write(f"{title},{author},{year},Not Read\n")
  
  # line break
  print(f"\n{title} ({year}) by {author} - Not Read\n")


def print_reading_list() :
  # get books
  reading_list = get_books()

  # list the books
  if reading_list :
    list_books(reading_list)
  else :
    print("\nNo books in the reading list\n")


def search_books() :
  # find books
  found_books = find_books()

  # print
  if found_books :
    list_books(found_books)
  else :
    print("No books found")


def mark_read(reading_list, book) :
  mod_index = reading_list.index(book)
  
  if reading_list[mod_index]['read'] == "Not Read" :
    reading_list[mod_index]['read'] = "Read"
    print(f"{book['title']} marked Read\n")
  else :
    print(f"{book['title']} already read\n")


def delete_book(reading_list, book) :
  title = book['title']
  reading_list.remove(book)
  print(f"{title} removed")


def modify_reading_list(operation) :
  # get books
  reading_list = get_books()
  
  # search for term in each title
  found_books = find_books()
  
  # 1st result found, operation performed
  if found_books :
    operation(reading_list, found_books[0])

    # write back to file
    with open("books2.csv", "w") as f :
      f.write("title,author,year,read\n")
      for book in reading_list : 
        f.write(",".join(book.values()) + "\n")
  
  # if result not found
  else :
    print("No book found")


user_prompt = '''\nPlease enter one of the following options:

- 'a' to add a book
- 'l' to list the books
- 's' to search for book(s) by title
- 'r' to mark a book (searched by title) as read
- 'd' to delete a book (searched by title)
- 'q' to quit
 
What would you like to do? '''

while (True) :
  user_input = input(user_prompt).strip().lower()

  if user_input == 'a' :
    add_book()
  
  elif user_input == 'l' :
    print_reading_list()

  elif user_input == 's' :
    search_books()
  
  elif user_input == 'r' :
    modify_reading_list(mark_read)
  
  elif user_input == 'd' :
    modify_reading_list(delete_book)

  elif user_input == 'q' :
    print("Quit")
    break
  
  else :
    print("Invalid input")
# Users should be able to add a book to their reading list by providing a book title, an author's name, and a year of publication.
# The program should store information about all of these books in a file called books.csv, and this data should be stored in CSV format.
# Users should be able to retrieve the books in their reading list, and these books should be printed out in a user-friendly format.
# Users should be able to search for a specific book by providing a book title.
# Users should be able to select these options from a text menu, and they should be able to perform multiple operations without restarting the program. You can see an example of a working menu in the post on while loops (day 8).

menu_prompt = """Please enter one of the following options:

- 'a' to add a book
- 'l' to list the books
- 's' to search for book(s) by title
- 'q' to quit

What would you like to do? """

# getting data from file
def get_data() :
  reading_list = []
  
  with open("books.csv", "r") as f:
    books_data = f.readlines()

    headers = books_data[0].strip().split(",")

    for row in books_data[1:]:
      reading_list.append(dict(zip(headers,row.strip().split(","))))
  
  return reading_list


# function to add books
def add_book() :

  # getting input from user
  title = input("\nEnter the book's name: ").strip()
  author = input("Enter the author's name: ").strip()
  year = int(input("Enter the year of publication: ").strip())

  # appending to book.csv (csv file)
  with open("books.csv", "a") as f:
    f.write(f"\n{title},{author},{year}")
  
  # confirming
  print("Added\n")


# function to read from reading_list
def print_reading_list(reading_list) :
  print("\n-----------------------------------------------------\nList:")
  
  for book in reading_list :
    name, author, year = book.values()
    print(f"{name} ({year}) by {author}")
  
  print("-----------------------------------------------------\n")


# function to search for book by title
def search_by_title(search_term) :

  reading_list = get_data()
  matching_books = []

  for book in reading_list :
    if search_term in book["title"].lower() :
      matching_books.append(book)
  
  return matching_books


# start of program
# start with menu prompt, perform chosen operation (or warn of invalid input) and continue the loop if break is not encountered
while (True) :
  choice = input(menu_prompt).strip().lower()

  if choice == 'a' :
    add_book()
  
  elif choice == 'l' :
    reading_list = get_data()
    if reading_list:
      print_reading_list(reading_list)
    else:
      print("No books in reading list")

  elif choice == 's' :
    print("\n-----------------------------------------------------Found\n")

    if get_data():
      search_title = input("Enter title of book you want to search for: ").strip().lower()

      results = search_by_title(search_title)
      if results:
        print_reading_list(results)
      else:
        print("No books found")

    else:
      print("No books in reading list")

    print("\n-----------------------------------------------------\n")

  elif choice == 'q' :
    break

  else : 
    print("Invalid input\n") 
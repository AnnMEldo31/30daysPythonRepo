# Users should be able to add a book to their reading list by providing a book title, an author's name, and a year of publication.
# The program should store information about all of these books in a Python list.
# Users should be able to display all the books in their reading list, and these books should be printed out in a user-friendly format.
# Users should be able to select these options from a text menu, and they should be able to perform multiple operations without restarting the program. You can see an example of a working menu in the post on while loops (day 8).

menu_prompt = """Please enter one of the following options:

- 'a' to add a book
- 'l' to list the books
- 'q' to quit

What would you like to do? """

reading_list = []

def add_book() :
  print()

  title = input("Enter the book's name: ").strip()
  author_name = input("Enter the author's name: ").strip()
  publ_year = int(input("Enter the year of publication: ").strip())

  reading_list.append({
    "title": title,
    "author": author_name,
    "year": publ_year
  })
  print("Added\n")


def print_reading_list() :
  print("\n-----------------------------------------------------")
  
  print("List: ")
  for book in reading_list :
    name, author, year = book.values()
    print(f"{name} ({year}) by {author}")
  
  print("-----------------------------------------------------\n")


while (True) :
  choice = input(menu_prompt).strip().lower()

  if choice == 'a' :
    add_book()
  
  elif choice == 'l' :
    if reading_list:
      print_reading_list()
    else:
      print("No books in reading list")

  elif choice == 'q' :
    break

  else : 
    print("Invalid input\n")
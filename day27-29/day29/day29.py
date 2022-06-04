from functools import wraps


# Make a decorator which calls a given function twice.
# You can assume the functions don't return anything important, but they may take arguments.
def call_twice(func):
    @wraps(func)
    def inner(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)

    return inner


@call_twice
def print_string(text="World"):
    print("Hello " + str(text))


print_string("Jane Doe")

print()

print_string()

print("-" * 100 + '\n')

# Imagine you have a list called books, which several functions in your application interact with.
# Write a decorator which causes your functions to run only if books is not empty.
books = []


def run_only_if_books_list_not_empty(func):
    @wraps(func)
    def inner(*args, **kwargs):
        if books:
            return func(*args, **kwargs)
        else:
            print(f"Books list is empty. Could not perform {func.__name__}")

    return inner


@run_only_if_books_list_not_empty
def delete_last_book():
    del books[-1]


@run_only_if_books_list_not_empty
def get_first_book_all_caps():
    return books[0].upper()


print(books)
print()

delete_last_book()
print(books)
print(get_first_book_all_caps())
print()

books.append("Autobiography")
books.append("Novella")
books.append("Anthology")

print(books)
print()

delete_last_book()
print(books)
print(get_first_book_all_caps())

print("-" * 100 + '\n')


# Write a decorator called printer which causes any decorated function to print their return values.
# If the return value of a given function is None, printer should do nothing.
def printer(func):
    @wraps(func)
    def inner(*args, **kwargs):
        result = func(*args, **kwargs)
        if result is not None:
            print(result)

    return inner


@printer
def returns_truthy_value():
    print("This function returns a truthy value")
    return 65


@printer
def does_not_return_value():
    print("This function does not return a value")


@printer
def returns_falsy_value_not_none():
    print("This function returns a falsy value that is not None")
    return []


returns_truthy_value()

print()

returns_falsy_value_not_none()

print()

does_not_return_value()

print("-" * 100 + '\n')

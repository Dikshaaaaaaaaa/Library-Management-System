def check_book_availability(book_list, book_name):
    for book in book_list:
        print(f"Checking: {book.lower()} vs {book_name.lower()}")
        if book.lower() == book_name.lower():
            return "Book is available!"
    return "Book is not available."

books = ["Python Programming", "Data Structures", "Algorithms"]
print(check_book_availability(books, "python"))


from collections.abc import Sequence

from books import Book

VALID_MENU_CHOICES = {"1", "2", "3", "4", "5"}
INVALID_MENU_CHOICE_MESSAGE = "Invalid choice. Please enter a number from 1 to 5."


def print_menu() -> None:
    print("\n📚 Book Collection App")
    print("1. Add a book")
    print("2. List books")
    print("3. Mark book as read")
    print("4. Remove a book")
    print("5. Exit")


def get_user_choice() -> str:
    while True:
        choice = input("Choose an option (1-5): ").strip()
        if not choice or not choice.isdigit():
            print(INVALID_MENU_CHOICE_MESSAGE)
            continue

        if choice not in VALID_MENU_CHOICES:
            print(INVALID_MENU_CHOICE_MESSAGE)
            continue

        return choice


def _get_required_input(prompt: str, field_name: str) -> str:
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print(f"{field_name} cannot be empty.")


def get_book_details() -> tuple[str, str, int]:
    title = _get_required_input("Enter book title: ", "Title")
    author = _get_required_input("Enter author: ", "Author")

    while True:
        year_input = input("Enter publication year: ").strip()
        if not year_input:
            return title, author, 0

        try:
            year = int(year_input)
        except ValueError:
            print("Invalid year. Please enter a whole number.")
            continue

        if year < 0:
            print("Invalid year. Please enter 0 or a positive number.")
            continue

        return title, author, year


def print_books(books: Sequence[Book]) -> None:
    if not books:
        print("No books in your collection.")
        return

    print("\nYour Books:")
    for index, book in enumerate(books, start=1):
        status = "✅ Read" if book.read else "📖 Unread"
        print(f"{index}. {book.title} by {book.author} ({book.year}) - {status}")

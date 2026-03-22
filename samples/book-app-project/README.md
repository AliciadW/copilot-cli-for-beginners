# Book Collection App

*(This README is intentionally rough so you can improve it with GitHub Copilot CLI)*

A Python app for managing books you have or want to read.
It can add, remove, list, and search books.

---

## Current Features

* Reads books from a JSON file (our database)
* Searches books by partial title or author match
* Input checking is weak in some areas
* Some tests exist but probably not enough

---

## Files

* `book_app.py` - Main CLI entry point
* `books.py` - BookCollection class with data logic
* `utils.py` - Helper functions for UI and input
* `data.json` - Sample book data
* `tests/test_books.py` - Starter pytest tests

---

## Running the App

```bash
python book_app.py list
python book_app.py add
python book_app.py find
python book_app.py remove
python book_app.py help
```

`find` now searches by either title or author, using partial and case-insensitive matching.
For example, `hob` matches `The Hobbit`, and `orwell` matches `George Orwell`.

## Running Tests

```bash
python -m pytest tests/
```

---

## Notes

* Not production-ready (obviously)
* Some code could be improved
* Could add more commands later

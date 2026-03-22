import importlib
import os
import sys

import pytest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import books
from books import Book


@pytest.fixture(autouse=True)
def use_temp_data_file(tmp_path, monkeypatch):
    """Use a temporary data file for each test."""
    temp_file = tmp_path / "data.json"
    temp_file.write_text("[]")
    monkeypatch.setattr(books, "DATA_FILE", str(temp_file))


@pytest.fixture
def book_app():
    sys.modules.pop("book_app", None)
    return importlib.import_module("book_app")


def test_main_dispatches_to_command_handler(book_app, monkeypatch):
    called = []

    monkeypatch.setattr(sys, "argv", ["book_app.py", "list"])
    monkeypatch.setattr(book_app, "COMMAND_HANDLERS", {"list": lambda: called.append("list")})

    book_app.main()

    assert called == ["list"]


def test_main_shows_help_for_unknown_command(book_app, monkeypatch, capsys):
    monkeypatch.setattr(sys, "argv", ["book_app.py", "unknown"])

    book_app.main()

    output = capsys.readouterr().out
    assert "Unknown command." in output
    assert "Book Collection Helper" in output


def test_handle_find_searches_books_by_title_or_author(book_app, monkeypatch, capsys):
    called = []
    expected_books = [Book(title="The Hobbit", author="J.R.R. Tolkien", year=1937)]

    monkeypatch.setattr("builtins.input", lambda _: "hob")
    monkeypatch.setattr(
        book_app.collection,
        "search_books",
        lambda query: called.append(query) or expected_books,
    )

    book_app.handle_find()

    output = capsys.readouterr().out
    assert called == ["hob"]
    assert "Search Books" in output
    assert "The Hobbit by J.R.R. Tolkien (1937)" in output


def test_show_help_describes_title_or_author_search(book_app, capsys):
    book_app.show_help()

    output = capsys.readouterr().out
    assert "find     - Search books by title or author" in output

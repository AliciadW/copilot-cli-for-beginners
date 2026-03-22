import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import get_book_details, get_user_choice


class TestGetUserChoice:
    """Tests for get_user_choice."""

    def test_retries_until_choice_is_valid(self, monkeypatch, capsys):
        responses = iter(["", "9", "2"])
        monkeypatch.setattr("builtins.input", lambda _: next(responses))

        choice = get_user_choice()

        assert choice == "2"
        captured = capsys.readouterr()
        assert captured.out.count("Invalid choice. Please enter a number from 1 to 5.") == 2


class TestGetBookDetails:
    """Tests for get_book_details."""

    def test_retries_on_empty_fields_and_invalid_year(self, monkeypatch, capsys):
        responses = iter(["", "Dune", "", "Frank Herbert", "abc", "-1", "1965"])
        monkeypatch.setattr("builtins.input", lambda _: next(responses))

        details = get_book_details()

        assert details == ("Dune", "Frank Herbert", 1965)
        captured = capsys.readouterr()
        assert "Title cannot be empty." in captured.out
        assert "Author cannot be empty." in captured.out
        assert "Invalid year. Please enter a whole number." in captured.out
        assert "Invalid year. Please enter 0 or a positive number." in captured.out

    def test_blank_year_defaults_to_zero(self, monkeypatch):
        responses = iter(["Dune", "Frank Herbert", ""])
        monkeypatch.setattr("builtins.input", lambda _: next(responses))

        details = get_book_details()

        assert details == ("Dune", "Frank Herbert", 0)

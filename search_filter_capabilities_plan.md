# Plan: add search and filter capabilities to the book app

## Problem

The primary Python sample app can list books, add/remove books, and find books by author, but it does not provide a broader search/filter experience for common user questions like "show unread books" or "find a title that contains a word." The current CLI also exposes only one narrow lookup command (`find` by exact author name), so discovery workflows are limited.

## Proposed approach

Add richer query support to the Python sample app by extending `BookCollection` with reusable search/filter helpers and exposing them through `samples/book-app-project/book_app.py`. The first version will support title keyword search plus author and read/unread status filters. Update tests and the sample README so the new CLI workflow is documented and covered.

## Todos

1. Audit the current query-related flow in `samples/book-app-project/book_app.py` and `samples/book-app-project/books.py`, especially the existing `find_by_author` behavior, to determine the cleanest extension point for broader search/filter support.
2. Add reusable collection-level helpers for the chosen search/filter scope without changing the JSON storage model.
3. Update the CLI entry point to expose the new search/filter workflow with clear prompts, command names, and help text.
4. Extend the sample's tests to cover the new search/filter behavior at the collection and CLI-facing levels.
5. Update `samples/book-app-project/README.md` so the documented commands and examples match the new query workflow.

## Notes

- Scope target remains the Python sample app plus related tests/docs.
- The existing app already has `find_by_author`, so the implementation should likely build on that instead of replacing the data model.
- Confirmed first-version scope: title keyword search plus author and read/unread status filters.

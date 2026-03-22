# Plan: add a "mark as read" command to the book app

## Problem

The primary Python sample app already supports marking a book as read at the data layer (`BookCollection.mark_as_read`), but the CLI entry point does not expose that capability as a command. The app help text and sample README also do not show a `mark-read` workflow, so the user-facing experience is incomplete.

## Proposed approach

Add a dedicated CLI command in `samples/book-app-project/book_app.py` that prompts for a title, calls the existing `BookCollection.mark_as_read` method, and gives clear success or not-found feedback. Then update the related tests and sample README so the command is documented and verified end to end.

## Todos

1. Audit the current CLI flow in `samples/book-app-project/book_app.py` and define how the new command should appear in dispatch, prompts, and help output while reusing the existing collection logic.
2. Update the Python sample app to add the new "mark as read" command and user feedback without changing the existing JSON storage model.
3. Extend the sample's tests to cover the new command path and confirm read status persists as expected.
4. Update `samples/book-app-project/README.md` so the documented commands match the app behavior.

## Notes

- Scope confirmed: Python sample app plus related tests/docs.
- `samples/book-app-project/books.py` already has `mark_as_read`, so no new persistence fields or storage format changes should be necessary.
- When implementation starts, validate with the sample project's existing pytest command.

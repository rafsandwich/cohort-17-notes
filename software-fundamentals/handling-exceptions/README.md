# Handling Exceptions

Error: something has gone wrong
Exception: something that breaks the normal flow of execution

1. [Tutorial: errors in Python](https://docs.python.org/3/tutorial/errors.html)
2. [Exception documentation](https://docs.python.org/3/library/exceptions.html)

## Exceptions

- `TypeError` (When you can't do that with that type of thing)
- `IndexError` (The thing you're trying to access is too short)
- `SyntaxError` (What you've written doesn't make sense)
- `ValueError` (This is the right kind of thing but not the right thing itself)
- `NameError` (This thing doesn't exist)
- `AttributeError` (This object does not have that property/method)
- `IndentationError` (Your code is laid out wrong)
- `ZeroDivisionError` (When you do maths bad)
- `OSError` (You broke the computer)
- `KeyboardInterrupt` (You stopped it)

## Raising Exceptions

- `raise` exceptions when something is wrong
- `raise` exceptions when it's not your (the current code's) problem
- Always `raise` exceptions as a new instance, with a clear message

## `try...except`

- Rarely use it
- Appropriate when
  - You can't avoid the error
  - You do know about it
  - You have a specific plan to handle the problem
- If you don't have a plan, let the program crash

## Testing Exceptions

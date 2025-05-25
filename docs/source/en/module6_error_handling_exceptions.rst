.. _module6-error-handling-exceptions:

============================================================
Module 6: Error Handling and Exceptions - Graceful Recovery
============================================================

Welcome to Module 6! So far, we've written programs that, for the most part, assume everything goes according to plan. However, in the real world, programs encounter unexpected situations: users might enter invalid data, files might be missing, or network connections might drop. **Error handling** is the process of anticipating, detecting, and responding to these errors in a way that allows your program to either recover gracefully or terminate with a clear message, rather than crashing abruptly. Python uses **exceptions** to manage these runtime errors.

.. image:: ../_static/images/safety_net.png
   :alt: A safety net under a tightrope walker, representing exception handling
   :width: 600px
   :align: center

Learning Objectives
-------------------

By the end of this module, you will be able to:

*   Understand the difference between syntax errors and exceptions (runtime errors).
*   Identify common types of built-in exceptions in Python.
*   Use `try` and `except` blocks to catch and handle exceptions.
*   Handle multiple specific exceptions.
*   Access the exception object to get more information about an error.
*   Use the `else` clause in a `try` block to execute code when no exceptions occur.
*   Use the `finally` clause to execute cleanup code regardless of whether an exception occurred.
*   Raise exceptions deliberately using the `raise` statement.
*   Understand best practices for exception handling.

----------------------------------------------------

What are Errors and Exceptions?
===============================

In programming, errors can be broadly categorized:

1.  **Syntax Errors (Parsing Errors):**
    These occur when your code violates Python's grammatical rules. The Python interpreter detects these errors *before* your program even starts running. You've likely encountered these already (e.g., missing colons, incorrect indentation, misspelled keywords). The program will not run until syntax errors are fixed.

    .. code-block:: python

        # Syntax Error: Missing colon
        # def my_function()
        #    print("Hello")

        # Syntax Error: Invalid syntax
        # print "Hello" # In Python 3, print is a function

2.  **Runtime Errors (Exceptions):**
    These errors occur *while* your program is running. Even if your code is syntactically correct, it might encounter situations it can't handle, leading to an exception. When an exception occurs and is not handled, the program terminates and Python prints a "traceback" message, indicating where the error happened.

    .. code-block:: python

        # Example of a runtime error (ZeroDivisionError)
        # numerator = 10
        # denominator = 0
        # result = numerator / denominator # This line will raise a ZeroDivisionError
        # print(result)

        # Example of a runtime error (TypeError)
        # age = 30
        # message = "My age is: " + age # This line will raise a TypeError (can't concatenate str and int)
        # print(message)

An **exception** is an event, which occurs during the execution of a program, that disrupts the normal flow of the program's instructions. When a Python script raises an exception, it must either handle the exception immediately or terminate.

Common Built-in Exceptions
--------------------------
Python has many built-in exceptions. Some common ones include:

*   `TypeError`: Operation or function applied to an object of inappropriate type. (e.g., ` "2" + 2`)
*   `ValueError`: Operation or function receives an argument with the right type but an inappropriate value. (e.g., `int("hello")`)
*   `NameError`: A local or global name is not found. (e.g., using an undefined variable)
*   `IndexError`: A sequence subscript is out of range. (e.g., `my_list[10]` when `my_list` has only 3 elements)
*   `KeyError`: A dictionary key is not found. (e.g., `my_dict["unknown_key"]`)
*   `ZeroDivisionError`: Second argument of a division or modulo operation is zero.
*   `FileNotFoundError`: A file or directory is requested but doesn’t exist.
*   `AttributeError`: An attribute reference or assignment fails. (e.g., ` "string".append("x")`)
*   `ImportError`: The `import` statement has trouble trying to load a module.

----------------------------------------------------

Handling Exceptions: The `try-except` Block
============================================

To handle exceptions gracefully, you use the `try` and `except` keywords.

*   The code that might cause an exception is placed in the `try` block.
*   If an exception occurs within the `try` block, Python looks for a matching `except` block to handle it.
*   If no exception occurs, the `except` block is skipped.

Basic Syntax:
-------------
.. code-block:: python

    try:
        # Code that might raise an exception
        # ...
    except ExceptionType: # Catches a specific type of exception
        # Code to handle the exception
        # ...

Example: Handling `ValueError`
------------------------------
Let's say we want to get an integer from the user. `int()` will raise a `ValueError` if the input cannot be converted to an integer.

.. code-block:: python

    try:
        age_str = input("Enter your age: ")
        age = int(age_str) # Potential ValueError
        print(f"You will be {age + 1} next year.")
    except ValueError:
        print("Invalid input. Please enter a whole number for age.")

If the user enters "thirty", the `int("thirty")` call raises a `ValueError`. The `except ValueError:` block catches this, and its code is executed. If the user enters "30", no exception occurs, and the `except` block is skipped.

Handling Specific Exceptions
----------------------------
It's good practice to catch specific exceptions rather than using a bare `except:` clause (which catches *all* exceptions). This allows you to respond appropriately to different types of errors.

.. code-block:: python

    try:
        num1 = int(input("Enter a numerator: "))
        num2 = int(input("Enter a denominator: "))
        result = num1 / num2 # Potential ZeroDivisionError or ValueError
        print(f"The result is: {result}")
    except ValueError:
        print("Invalid input. Please enter numbers only.")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except Exception as e: # Catch any other unexpected exceptions
        print(f"An unexpected error occurred: {e}")

*   Python tries the `except` clauses one by one.
*   The `Exception as e` part is useful:
    *   `Exception` is a base class for most built-in exceptions. Catching it is a bit general but better than a bare `except:`.
    *   `as e` assigns the exception instance to the variable `e`, allowing you to access information about the error (e.g., `print(e)` often gives the error message).

Multiple Exceptions in a Single `except` Block
---------------------------------------------
You can handle multiple exception types with a single block by providing them as a tuple.

.. code-block:: python

    filename = "my_data.txt"
    try:
        with open(filename, "r") as f:
            content = f.read()
            value = int(content.strip())
        print(f"Value from file: {value}")
    except (FileNotFoundError, ValueError) as e:
        print(f"Error processing file '{filename}': {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

----------------------------------------------------

The `else` Clause
=================

The `try` statement can optionally have an `else` clause. The code in the `else` block is executed *only if* the `try` block does not raise an exception.

.. code-block:: python

    try:
        num_str = input("Enter a number: ")
        num = float(num_str)
    except ValueError:
        print("That was not a valid number.")
    else:
        # This block runs only if no ValueError occurred in the try block
        print(f"The square of your number is: {num ** 2}")

Why use `else`? It helps to separate the code that might raise an exception from the code that should run only if the initial operations were successful, improving readability.

----------------------------------------------------

The `finally` Clause
====================

The `try` statement can also have a `finally` clause. The code in the `finally` block is *always* executed, regardless of whether an exception occurred in the `try` block or if it was handled. This is often used for cleanup actions, like closing files or releasing resources.

.. code-block:: python

    file = None # Initialize file to None
    try:
        file_path = "data.txt"
        file = open(file_path, "w") # Potential FileNotFoundError if mode was 'r' and file didn't exist
                                     # or PermissionError if no write access
        file.write("Hello, world!")
        # Simulate an error:
        # result = 10 / 0 # This would cause a ZeroDivisionError
        print("Successfully wrote to file.")
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except ZeroDivisionError:
        print("Error: Calculation error (division by zero).")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        # This block always executes
        if file: # Check if file was successfully opened
            file.close()
            print("File closed.")
        else:
            print("File was not opened, so no need to close.")

Even if an unhandled exception occurs in the `try` or `except` block, or if a `return`, `break`, or `continue` statement is executed, the `finally` clause will still run before the program truly exits or continues elsewhere.

The `with` statement (seen in Module 4 for files) often handles resource cleanup automatically and can be a cleaner alternative to `try...finally` for managing resources like files.

----------------------------------------------------

Raising Exceptions: The `raise` Statement
=========================================

You can deliberately raise an exception in your code using the `raise` statement. This is useful when you detect an error condition in your function and want to signal it to the calling code.

Syntax: `raise ExceptionType("Optional error message")`

.. code-block:: python

    def get_age(age_val):
        """Returns the age if valid, otherwise raises a ValueError."""
        if age_val < 0:
            raise ValueError("Age cannot be negative.")
        if age_val > 120:
            raise ValueError("Age seems too high, please verify.")
        return age_val

    try:
        user_age_input = int(input("Enter your age: "))
        valid_age = get_age(user_age_input)
        print(f"Age validated: {valid_age}")
    except ValueError as e: # Catches ValueError from int() or from get_age()
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

You can raise built-in exceptions or even define your own custom exceptions (which is a more advanced topic, typically involving creating classes that inherit from `Exception`).

----------------------------------------------------

Best Practices for Exception Handling
=====================================

1.  **Be Specific:** Catch specific exceptions whenever possible, rather than a bare `except:` or `except Exception:`. This makes your error handling more precise.
2.  **Don't Silence Errors:** Avoid catching exceptions just to ignore them (e.g., `except: pass`), unless you have a very good reason. This can hide bugs.
3.  **Use `finally` for Cleanup:** Ensure resources are released (files closed, locks released) in a `finally` block or by using context managers (`with` statement).
4.  **Provide Informative Messages:** When you handle or raise exceptions, give clear messages that help diagnose the problem.
5.  **Fail Fast (Sometimes):** If an error occurs that your current function cannot reasonably handle, it's often better to let the exception propagate (or raise a new, more specific one) rather than trying to guess a recovery.
6.  **Keep `try` Blocks Small:** Enclose only the specific lines of code that might raise an exception in the `try` block. This makes it clearer where the error might originate.
7.  **Use `else` for Success Code:** Place code that should run only if the `try` block succeeds in the `else` clause.

----------------------------------------------------

Mini-Project: Robust Data Processor
===================================

Let's create a small program that simulates processing data items. The processing function might encounter issues with certain data.

**Goal:**
1.  Create a function `process_item(item)`:
    *   If `item` is `None`, it should `raise TypeError` with a message "Item cannot be None."
    *   If `item` is a string that cannot be converted to a number, trying `float(item)` will raise `ValueError`.
    *   If `item` (after conversion to float) is negative, it should `raise ValueError` with a message "Item value cannot be negative for processing."
    *   If `item` is 0, it should `raise ZeroDivisionError` (simulating a division step that fails for zero).
    *   If successful, it should return, say, the square root of the item (use `math.sqrt`, so you'll need `import math`).
2.  The main part of the program should:
    *   Have a list of sample data items (e.g., `[16, "25", "apple", -4, 0, None, 49]`).
    *   Loop through each item.
    *   For each item, call `process_item` inside a `try-except-else-finally` structure.
    *   Handle `TypeError`, `ValueError`, and `ZeroDivisionError` specifically, printing an informative message.
    *   Use an `else` block to print the successful result.
    *   Use a `finally` block to print a message like "Finished processing attempt for item: [item_value]".

**Example Snippet of Interaction for one item:**

.. code-block:: text

    Processing item: 16
    Successfully processed. Result: 4.0
    Finished processing attempt for item: 16
    ---
    Processing item: apple
    Error processing item 'apple': could not convert string to float: 'apple'
    Finished processing attempt for item: apple
    ---
    Processing item: -4
    Error processing item '-4': Item value cannot be negative for processing.
    Finished processing attempt for item: -4
    ---

.. admonition:: Solution (Try it yourself before looking!)
   :class: dropdown

   .. code-block:: python

       # robust_data_processor.py
       import math

       def process_item(item):
           """
           Processes a single data item.
           Raises TypeError, ValueError, or ZeroDivisionError for invalid items.
           Returns the square root of the item if valid.
           """
           print(f"Processing item: {repr(item)}") # repr() shows None as 'None'

           if item is None:
               raise TypeError("Item cannot be None.")

           try:
               # Attempt to convert to float if it's a string or already a number
               numeric_item = float(item)
           except ValueError as e: # Handles cases like float("apple")
               # Re-raise or raise a new, more specific error if needed,
               # or let the original ValueError propagate with its message.
               # For this example, we'll let the original 'could not convert...' message go.
               raise ValueError(f"Could not convert '{item}' to a number: {e}")


           if numeric_item < 0:
               raise ValueError("Item value cannot be negative for processing.")
           if numeric_item == 0:
               # Simulate an operation that would cause this, or just raise it.
               # For example, if we were calculating 1/sqrt(item)
               raise ZeroDivisionError("Item value is zero, leading to division by zero in a hypothetical step.")

           return math.sqrt(numeric_item)

       def main():
           """Main function to test the data processor."""
           data_samples = [16, "25", "apple", -4, 0, None, 49, "7.5"]

           for sample in data_samples:
               result = None
               try:
                   result = process_item(sample)
               except TypeError as e:
                   print(f"Type Error for item '{repr(sample)}': {e}")
               except ValueError as e:
                   print(f"Value Error for item '{repr(sample)}': {e}")
               except ZeroDivisionError as e:
                   print(f"Zero Division Error for item '{repr(sample)}': {e}")
               except Exception as e: # Catch-all for any other unexpected errors
                   print(f"An unexpected error occurred for item '{repr(sample)}': {e}")
               else:
                   print(f"Successfully processed. Result: {result}")
               finally:
                   print(f"Finished processing attempt for item: {repr(sample)}")
                   print("---")

       if __name__ == "__main__":
           main()

----------------------------------------------------

Module 6 Summary
================

Well done on navigating Module 6! Understanding and implementing error handling is crucial for writing robust and user-friendly Python programs. You've learned:

*   The distinction between **syntax errors** and **runtime errors (exceptions)**.
*   How to use `try-except` blocks to catch and manage specific exceptions.
*   The role of the `else` clause for code that should run when no exceptions occur.
*   The importance of the `finally` clause for cleanup operations that must always execute.
*   How to `raise` exceptions to signal error conditions within your code.
*   Key **best practices** for effective exception handling.

By anticipating potential problems and handling them gracefully, you can prevent your programs from crashing unexpectedly and provide better feedback to users or other parts of your system.

In the next module, we'll explore how to work with files, reading data from them and writing data to them, where exception handling will be particularly relevant: :ref:`module7-file-io`!
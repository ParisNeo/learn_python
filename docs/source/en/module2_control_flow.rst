.. _module2-control-flow:

================================================================
Module 2: Control Flow - Making Decisions and Repeating Actions
================================================================

Welcome to Module 2! In the previous module, we learned how to store and manage data using variables and different data types. Now, we'll explore how to control the *flow* of our programs. This means making decisions based on certain conditions and repeating tasks efficiently. These are fundamental concepts that give your programs intelligence and power.

.. image:: /_static/images/flowchart_decision.png
   :alt: Flowchart showing a decision point and a loop
   :width: 300px
   :align: center

Learning Objectives
-------------------

By the end of this module, you will be able to:

*   Understand and use conditional statements (`if`, `elif`, `else`) to make decisions.
*   Utilize comparison operators (`==`, `!=`, `>`, `<`, `>=`, `<=`) to form conditions.
*   Employ logical operators (`and`, `or`, `not`) to combine multiple conditions.
*   Understand the concept of "truthiness" in Python.
*   Implement `for` loops to iterate over sequences (like strings or ranges of numbers).
*   Use the `range()` function to generate sequences for loops.
*   Implement `while` loops to repeat code as long as a condition is true.
*   Control loop execution with `break` and `continue` statements.
*   Write simple programs that involve decision-making and repetition.

----------------------------------------------------

What is Control Flow?
=====================

By default, Python programs execute statements one after another, from top to bottom. **Control flow** refers to the order in which these statements are executed. Control flow statements allow you to:

1.  **Make Decisions:** Execute certain blocks of code only if specific conditions are met. (e.g., "If the user is an admin, show the admin panel.")
2.  **Repeat Actions:** Execute a block of code multiple times. (e.g., "For every item in a shopping list, print its name.")

----------------------------------------------------

Conditional Statements: `if`, `elif`, `else`
===========================================

Conditional statements allow your program to choose different paths based on whether a condition is `True` or `False`.

The `if` Statement
------------------
The simplest form of decision-making. The code block indented under the `if` statement only executes if the `condition` is `True`.

.. code-block:: python

    age = 20
    if age >= 18:
        print("You are eligible to vote.")
        print("Please register if you haven't already.")

    print("This line always executes, regardless of the condition.")

*   The `condition` (`age >= 18`) is followed by a colon (`:`).
*   The code to be executed if the condition is true is **indented** (usually 4 spaces). Indentation is crucial in Python; it defines code blocks.

The `else` Statement
--------------------
Often, you want to do one thing if a condition is true and something else if it's false. The `else` statement handles this.

.. code-block:: python

    temperature = 15
    if temperature > 25:
        print("It's a hot day!")
    else:
        print("It's not a hot day. Maybe it's cool or cold.")

    # The code under else executes only if the if condition (temperature > 25) is False.

The `elif` Statement (Else If)
-------------------------------
When you have multiple conditions to check in sequence, you can use `elif`. Python checks `elif` conditions only if the preceding `if` or `elif` conditions were `False`.

.. code-block:: python

    score = 85
    if score >= 90:
        grade = "A"
    elif score >= 80: # This is checked only if score < 90
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:             # This executes if all preceding conditions are False
        grade = "F"

    print(f"Your grade is: {grade}") # Output: Your grade is: B

Comparison Operators
--------------------
Used to compare values and form conditions. They return a Boolean (`True` or `False`).

*   `==` : Equal to
*   `!=` : Not equal to
*   `>`  : Greater than
*   `<`  : Less than
*   `>=` : Greater than or equal to
*   `<=` : Less than or equal to

.. code-block:: python

    x = 10
    y = 5
    print(x == 10)    # True
    print(x != y)     # True
    print(x > y)      # True
    print(x < 5)      # False
    print(y >= 5)     # True

Logical Operators
-----------------
Used to combine multiple Boolean expressions:

*   `and`: Returns `True` if **both** expressions are true.
*   `or`:  Returns `True` if **at least one** expression is true.
*   `not`: Reverses the Boolean value ( `not True` is `False`, `not False` is `True`).

.. code-block:: python

    age = 22
    has_license = True

    # Can this person rent a car? (e.g., must be 21 or older AND have a license)
    if age >= 21 and has_license:
        print("Eligible to rent a car.")
    else:
        print("Not eligible to rent a car.")

    is_weekend = False
    has_homework = True
    if is_weekend or not has_homework:
        print("Time to relax!")
    else:
        print("Need to focus or do homework.")

Truthiness
----------
In Python, many values have an inherent "truthiness" or "falsiness" when used in a Boolean context (like an `if` condition).

*   **Falsy values:**
    *   `False` (the Boolean value)
    *   `None` (a special object representing absence of value)
    *   Zero of any numeric type (`0`, `0.0`)
    *   Empty sequences and collections: `""` (empty string), `[]` (empty list), `{}` (empty dictionary), `()` (empty tuple)
*   **Truthy values:** Pretty much everything else is considered `True`.

.. code-block:: python

    name = ""
    if name: # name is an empty string, which is Falsy
        print(f"Hello, {name}")
    else:
        print("Name is empty.") # This will be printed

    items_in_cart = 0
    if items_in_cart: # items_in_cart is 0, which is Falsy
        print("Proceed to checkout.")
    else:
        print("Your cart is empty.") # This will be printed

    my_list = [1, 2, 3]
    if my_list: # my_list is not empty, so it's Truthy
        print("List has items.") # This will be printed

Nested `if` Statements
----------------------
You can place `if` statements inside other `if` statements. This is useful for more complex decision-making.

.. code-block:: python

    is_logged_in = True
    user_role = "admin"

    if is_logged_in:
        print("Welcome!")
        if user_role == "admin":
            print("Admin dashboard access granted.")
        elif user_role == "editor":
            print("Content editing access granted.")
        else:
            print("Standard user access.")
    else:
        print("Please log in to continue.")

Be mindful of indentation with nested structures.

----------------------------------------------------

Loops: Repeating Actions
========================

Loops are used to execute a block of code repeatedly. Python has two main types of loops: `for` loops and `while` loops.

The `for` Loop
--------------
A `for` loop is used for iterating over a **sequence** (like a string, a list, a tuple) or other iterable objects.

**Iterating over a string:**

.. code-block:: python

    greeting = "Hello"
    for char_in_greeting in greeting: # 'char_in_greeting' is a variable you name
        print(char_in_greeting)
    # Output:
    # H
    # e
    # l
    # l
    # o

**Using `range()`:**
The `range()` function is often used with `for` loops to execute a block of code a specific number of times.

*   `range(stop)`: Generates numbers from 0 up to (but not including) `stop`.
    .. code-block:: python

        for i in range(5): # i will be 0, 1, 2, 3, 4
            print(f"Iteration number: {i}")

*   `range(start, stop)`: Generates numbers from `start` up to (but not including) `stop`.
    .. code-block:: python

        for i in range(2, 6): # i will be 2, 3, 4, 5
            print(i)

*   `range(start, stop, step)`: Generates numbers from `start` up to `stop`, incrementing by `step`.
    .. code-block:: python

        for i in range(0, 10, 2): # i will be 0, 2, 4, 6, 8
            print(i)

.. note::
    We'll learn more about **lists** (another common sequence type) in a later module. `for` loops are very powerful for working with lists:
    `my_list = [10, 20, 30]`
    `for item in my_list:`
    `    print(item)`

The `while` Loop
----------------
A `while` loop repeats a block of code as long as a given `condition` is `True`.

.. code-block:: python

    count = 0
    while count < 5:
        print(f"Count is: {count}")
        count = count + 1 # Important: Update the variable used in the condition!

    print("Loop finished.")
    # Output:
    # Count is: 0
    # Count is: 1
    # Count is: 2
    # Count is: 3
    # Count is: 4
    # Loop finished.

**Infinite Loops:**
If the condition in a `while` loop never becomes `False`, the loop will run forever. This is an **infinite loop**. You usually want to avoid these. If you accidentally create one, you can often stop it by pressing `Ctrl+C` in the terminal.

.. code-block:: python
    :emphasize-lines: 3

    # DANGER: Infinite Loop Example (don't run unless you know how to stop it)
    # while True:
    #     print("This will print forever!")
    #     # No way for True to become False here without a 'break'

Loop Control Statements
-----------------------

*   **`break`**: Immediately exits the current loop (both `for` and `while`).
    .. code-block:: python

        for i in range(10):
            if i == 5:
                print("Found 5, breaking out of the loop.")
                break # Exit the loop
            print(i)
        # Output: 0, 1, 2, 3, 4, Found 5, breaking out of the loop.

*   **`continue`**: Skips the rest of the code inside the current iteration of the loop and proceeds to the next iteration.
    .. code-block:: python

        for i in range(5):
            if i == 2:
                print("Skipping iteration 2.")
                continue # Skip the rest of this iteration
            print(f"Processing iteration {i}")
        # Output:
        # Processing iteration 0
        # Processing iteration 1
        # Skipping iteration 2.
        # Processing iteration 3
        # Processing iteration 4

*   **`else` Clause in Loops (Less Common):**
    Both `for` and `while` loops can have an `else` clause. The `else` block executes if the loop completes normally (i.e., it wasn't terminated by a `break` statement).

    .. code-block:: python

        for i in range(3):
            print(f"Looping: {i}")
        else:
            print("Loop completed without a break.")
        # Output:
        # Looping: 0
        # Looping: 1
        # Looping: 2
        # Loop completed without a break.

        num = 7
        search_val = 5
        while num > 0:
            if num == search_val:
                print(f"Found {search_val}!")
                break
            num -= 1
        else: # Executes only if the while loop condition becomes false (num <= 0)
              # AND break was not encountered
            print(f"{search_val} not found in the countdown.")


----------------------------------------------------

Mini-Project: Number Guessing Game
==================================

Let's combine `if/elif/else` and `while` loops to create a simple number guessing game.

**Goal:**
1.  The computer will "think" of a secret number (e.g., between 1 and 10).
2.  The user will try to guess the number.
3.  The program will tell the user if their guess is too high, too low, or correct.
4.  The game continues until the user guesses correctly.
5.  (Optional) Count the number of guesses.

**Steps:**

1.  **Choose a secret number.** For now, you can hardcode it (assign it directly to a variable). Later, we can learn how to make it random.
    `secret_number = 7`
2.  Use a `while True` loop to keep the game going until the user guesses correctly. Inside the loop, you'll use `break` to exit when they win.
3.  Inside the loop:
    *   Ask the user for their guess using `input()`.
    *   Convert the input to an integer using `int()`. Remember to handle potential `ValueError` if the user types non-numeric input (you can do this with a `try-except` block, or for simplicity in this early stage, assume valid input).
    *   Use `if/elif/else` to compare the guess with the `secret_number`.
    *   Print "Too high!", "Too low!", or "Correct!"
    *   If correct, print a congratulatory message and `break` out of the loop.
4.  (Optional) Initialize a `guesses_count` variable to 0 before the loop. Increment it inside the loop for each guess. Display it when the user wins.

**Example Interaction:**

.. code-block:: text

    Guess the number (between 1 and 10): 5
    Too low!
    Guess the number (between 1 and 10): 8
    Too high!
    Guess the number (between 1 and 10): 7
    Correct! You guessed it in 3 tries.

.. admonition:: Solution (Try it yourself before looking!)
   :class: dropdown

   .. code-block:: python

       # number_guessing_game.py

       secret_number = 7
       guesses_count = 0
       max_guesses = 5 # Optional: limit guesses

       print("Welcome to the Number Guessing Game!")
       print(f"I'm thinking of a number between 1 and 10. You have {max_guesses} tries.")

       while guesses_count < max_guesses:
           try:
               guess_str = input(f"Guess #{guesses_count + 1}: ")
               guess = int(guess_str)
           except ValueError:
               print("Invalid input. Please enter a number.")
               continue # Skip to the next iteration

           guesses_count += 1 # Increment guess count

           if guess < secret_number:
               print("Too low!")
           elif guess > secret_number:
               print("Too high!")
           else:
               print(f"Correct! You guessed the number {secret_number} in {guesses_count} tries.")
               break # Exit the loop since the guess is correct
       else:
           # This else clause for the while loop executes if the loop finished
           # because guesses_count reached max_guesses (and not due to a 'break')
           if guess != secret_number: # Check if they didn't guess it on the last try
                print(f"Sorry, you've run out of guesses. The number was {secret_number}.")

----------------------------------------------------

Module 2 Summary
================

Excellent! You've now learned how to make your Python programs much more dynamic:

*   **Conditional statements (`if`, `elif`, `else`)** allow your code to make decisions and execute different paths based on conditions.
*   **Comparison (`==`, `!=`, etc.) and logical (`and`, `or`, `not`) operators** are essential for building these conditions.
*   **`for` loops** are great for iterating over sequences or running code a fixed number of times (using `range()`).
*   **`while` loops** repeat code as long as a condition remains true, perfect for situations where you don't know the exact number of iterations beforehand.
*   **`break` and `continue`** give you finer control over loop execution.

With control flow, your programs can start to exhibit more complex and intelligent behavior. These are foundational tools you'll use in almost every Python program you write.

In the next module, we'll start organizing our data more effectively by learning about **data structures like lists and tuples**: :ref:`module3-data-structures-lists-tuples`!
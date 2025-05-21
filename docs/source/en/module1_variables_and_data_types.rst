.. _module1-variables-and-data-types:

=================================================
Module 1: Variables, Data Types, and User Input
=================================================

Welcome to Module 1! Now that you're set up and have written your first Python program, it's time to dive into how Python handles data. We'll explore variables (how to store information) and the different types of data you'll encounter. We'll also learn how to make your programs interactive by getting input from the user.

.. image:: /_static/images/data_blocks.png
   :alt: Colorful blocks representing different data types
   :width: 250px
   :align: center


Learning Objectives
-------------------

By the end of this module, you will be able to:

*   Understand what variables are and why they are used.
*   Declare and assign values to variables in Python.
*   Follow Python's naming rules and conventions for variables.
*   Identify and use fundamental Python data types:
    *   Integers (`int`)
    *   Floating-point numbers (`float`)
    *   Strings (`str`)
    *   Booleans (`bool`)
*   Use the `type()` function to determine a variable's data type.
*   Perform basic operations with numbers and strings (concatenation, f-strings).
*   Convert data from one type to another (type casting).
*   Get input from a user using the `input()` function.

----------------------------------------------------

What are Variables?
===================

In programming, a **variable** is like a labeled container or a box where you can store a piece of information (data). You give the variable a name, and then you can refer to the data by that name. This makes your code much more readable and flexible.

Imagine you're calculating the area of a rectangle. Instead of writing `5 * 10` everywhere, you could store the length and width in variables:

.. code-block:: python

    length = 10
    width = 5
    area = length * width
    print(area) # Output: 50

If you need to change the length or width, you only need to change it in one place (where the variable is assigned), and the rest of your code that uses that variable will automatically use the new value.

Assigning Values to Variables
-----------------------------

In Python, you create a variable and assign it a value using the equals sign (`=`):

.. code-block:: python

    # Variable_name = value
    my_age = 30
    user_name = "Alice"
    pi_value = 3.14159
    is_learning = True

    print(my_age)
    print(user_name)
    print(pi_value)
    print(is_learning)

*   `my_age` is a variable storing an integer.
*   `user_name` is a variable storing a sequence of characters (a string).
*   `pi_value` is a variable storing a number with a decimal point.
*   `is_learning` is a variable storing a truth value (Boolean).

You can change the value of a variable by reassigning it:

.. code-block:: python

    x = 10
    print(x) # Output: 10
    x = 20
    print(x) # Output: 20

Variable Naming Rules and Conventions
-------------------------------------

Python has rules for naming variables:

*   **Must start with a letter (a-z, A-Z) or an underscore (`_`).**
*   Cannot start with a number.
*   Can only contain alpha-numeric characters (a-z, A-Z, 0-9) and underscores.
*   Variable names are **case-sensitive** (`age`, `Age`, and `AGE` are three different variables).

**Conventions (Best Practices):**

*   Use **lowercase with words separated by underscores** (this is called `snake_case`).
    *   Good: `user_name`, `first_name`, `total_amount`
    *   Not recommended (but valid): `UserName`, `firstname`, `TotalAmount`
*   Choose meaningful and descriptive names.
    *   Good: `student_gpa`
    *   Bad: `x`, `val`, `sg` (unless the context is very clear)
*   Avoid using Python keywords (like `print`, `if`, `for`, `while`, `True`, `False`, `None`, etc.) as variable names. Your editor might highlight these.

----------------------------------------------------

Fundamental Data Types
======================

Python has several built-in data types. Let's look at the most common ones.

Integers (int)
--------------
Integers are whole numbers, positive or negative, without decimals.

.. code-block:: python

    count = 10
    negative_number = -5
    zero = 0
    print(type(count)) # Output: <class 'int'>

Floating-Point Numbers (float)
------------------------------
Floats represent real numbers and are written with a decimal point.

.. code-block:: python

    price = 19.99
    temperature = -3.5
    gravity = 9.8
    print(type(price)) # Output: <class 'float'>

Strings (str)
-------------
Strings represent sequences of characters (text). They are defined using either single quotes (`'...'`) or double quotes (`"..."`).

.. code-block:: python

    message = "Hello, Python learners!"
    name = 'Guido van Rossum'
    empty_string = ""

    print(type(message)) # Output: <class 'str'>

    # You can use quotes inside strings if they are different from the enclosing ones:
    quote1 = "He said, 'Python is fun!'"
    quote2 = 'She replied, "Indeed it is."'

    # For multi-line strings, use triple quotes ('''...''' or """..."""):
    multi_line_text = """This is a
    string that spans
    multiple lines."""
    print(multi_line_text)

Booleans (bool)
---------------
Booleans represent one of two values: `True` or `False`. They are crucial for making decisions in your code (which we'll cover later). Note the capitalization.

.. code-block:: python

    is_active = True
    has_permission = False
    print(type(is_active)) # Output: <class 'bool'>

Checking Data Types with `type()`
---------------------------------
You can use the built-in `type()` function to find out the data type of a variable or a value.

.. code-block:: python

    num = 42
    greeting = "Hi"
    pi = 3.14
    is_valid = True

    print(type(num))        # Output: <class 'int'>
    print(type(greeting))   # Output: <class 'str'>
    print(type(pi))         # Output: <class 'float'>
    print(type(is_valid))   # Output: <class 'bool'>
    print(type(2.0 + 5))    # What do you think this will be? (Hint: <class 'float'>)

----------------------------------------------------

Working with Data
=================

Basic Operations
----------------

**With Numbers (int, float):**
Python supports standard arithmetic operations:

.. code-block:: python

    a = 10
    b = 3

    sum_val = a + b        # Addition: 13
    diff_val = a - b       # Subtraction: 7
    prod_val = a * b       # Multiplication: 30
    div_val = a / b        # True Division: 3.333...
    floor_div_val = a // b # Floor Division (discards remainder): 3
    mod_val = a % b        # Modulus (remainder): 1
    exp_val = a ** b       # Exponentiation (a to the power of b): 1000

    print(f"Sum: {sum_val}")
    print(f"True Division: {div_val}")
    print(f"Floor Division: {floor_div_val}")
    print(f"Modulus: {mod_val}")

.. note::
   When you perform an operation with an `int` and a `float`, the result is usually a `float`.
   Example: `5 + 2.0` results in `7.0`.

**With Strings:**

*   **Concatenation (joining strings):** Use the `+` operator.
    .. code-block:: python

        first_name = "Ada"
        last_name = "Lovelace"
        full_name = first_name + " " + last_name
        print(full_name) # Output: Ada Lovelace

*   **String Repetition:** Use the `*` operator.
    .. code-block:: python

        separator = "-" * 10
        print(separator) # Output: ----------

*   **f-strings (Formatted String Literals):** A powerful and convenient way to embed expressions inside string literals. This is generally the preferred way to format strings.
    .. code-block:: python

        name = "Charlie"
        age = 7
        # Old way (concatenation, can be cumbersome)
        # greeting = "My dog's name is " + name + " and he is " + str(age) + " years old."

        # New way (f-string)
        greeting = f"My dog's name is {name} and he is {age} years old."
        print(greeting) # Output: My dog's name is Charlie and he is 7 years old.

    You place an `f` or `F` before the opening quote, and then you can put variables or expressions inside curly braces `{}`.

Type Conversion (Casting)
-------------------------
Sometimes you need to convert a value from one data type to another. This is called type casting.

*   `int(value)`: Converts `value` to an integer.
*   `float(value)`: Converts `value` to a float.
*   `str(value)`: Converts `value` to a string.

.. code-block:: python

    num_string = "100"
    # print(num_string + 5) # This would cause a TypeError! Can't add string and int.

    num_int = int(num_string)
    print(num_int + 5) # Output: 105

    num_float = float(num_string)
    print(num_float) # Output: 100.0

    number = 42
    num_as_str = str(number)
    print("The number is: " + num_as_str) # "The number is: 42"

    # Be careful:
    # int("hello") # This would cause a ValueError because "hello" cannot be converted to an int.
    # int("3.14")  # This would also cause a ValueError. Use float("3.14") first.
    print(int(float("3.14"))) # Output: 3

----------------------------------------------------

Getting User Input with `input()`
=================================

Programs often need to get information from the user. Python's `input()` function allows you to do this. It prompts the user to type something and then returns whatever they typed as a **string**.

.. code-block:: python

    user_name = input("Please enter your name: ")
    print(f"Hello, {user_name}!")

    # The input() function ALWAYS returns a string.
    age_str = input("Please enter your age: ")
    print(type(age_str)) # Output: <class 'str'>

    # If you need the age as a number, you must convert it:
    try:
        age_num = int(age_str)
        next_year_age = age_num + 1
        print(f"Next year, you will be {next_year_age} years old.")
    except ValueError:
        print("Invalid age entered. Please enter a number.")

.. tip::
   The `try-except` block in the example above is a way to handle potential errors (like the user typing "ten" instead of "10" for their age). We'll cover error handling in more detail later, but it's good to see it in context.

----------------------------------------------------

Mini-Project: Simple Info Collector
===================================

Let's put what you've learned into practice.

**Goal:** Write a Python program that:
1.  Asks the user for their name.
2.  Asks the user for their age.
3.  Asks the user for their favorite hobby.
4.  Prints a summary message using an f-string, like:
    "Hello [Name]! You are [Age] years old, and you enjoy [Hobby]. That's cool!"

**Example Interaction:**

.. code-block:: text

    Please enter your name: Bob
    Please enter your age: 25
    What is your favorite hobby? Coding
    Hello Bob! You are 25 years old, and you enjoy Coding. That's cool!

**Steps:**

1.  Create a new file (e.g., `info_collector.py`).
2.  Use `input()` to get the name, age, and hobby. Store them in variables.
3.  Remember that `input()` returns strings. If you plan to do any math with age (though not required for this specific project's output), you'd need to convert it to an `int`. For this project, using it as a string in the f-string is fine.
4.  Use an f-string and `print()` to display the summary message.
5.  Save and run your program.

.. admonition:: Solution (Try it yourself before looking!)
   :class: dropdown

   .. code-block:: python

       # info_collector.py
       # This program collects some information from the user and prints a summary.

       # 1. Ask for name
       user_name = input("Please enter your name: ")

       # 2. Ask for age
       user_age_str = input("Please enter your age: ")
       # For this project, we can keep age as a string for the output.
       # If we needed to do calculations, we'd convert it:
       # user_age_int = int(user_age_str)

       # 3. Ask for favorite hobby
       user_hobby = input("What is your favorite hobby? ")

       # 4. Print the summary message using an f-string
       summary_message = f"Hello {user_name}! You are {user_age_str} years old, and you enjoy {user_hobby}. That's cool!"
       print(summary_message)

----------------------------------------------------

Module 1 Summary
================

Fantastic work! You've covered a lot of ground in this module:

*   **Variables** are named containers for storing data.
*   You learned how to **name variables** following Python's rules and conventions (`snake_case`).
*   You were introduced to fundamental **data types**: `int`, `float`, `str`, and `bool`.
*   The `type()` function helps identify a variable's data type.
*   You can perform **basic operations** on numbers and strings, with **f-strings** being a great way to format output.
*   **Type casting** (`int()`, `float()`, `str()`) allows you to convert between data types.
*   The `input()` function lets your programs become **interactive** by getting data from the user (remembering it always returns a string).

These concepts are the building blocks for almost everything you'll do in Python. With variables and data types, you can start to represent and manipulate real-world information in your programs.

Next up, we'll learn how to control the flow of our programs and make decisions using :ref:`module2-control-flow`!
.. _module0-getting-started:

===========================================
Module 0: Getting Started - The Launchpad
===========================================

Welcome to your Python journey! This first module is all about getting you set up and comfortable with the very basics. We'll go from understanding what Python is to writing and running your very first program.

.. image:: ../_static/images/rocket_launch.png
   :alt: Rocket Launching - Your Python Journey Begins!
   :width: 200px
   :align: center


Learning Objectives
-------------------

By the end of this module, you will be able to:

*   Understand what programming is in simple terms.
*   Explain why Python is a great language to learn.
*   Successfully install Python on your computer.
*   Set up a basic code editor (VS Code recommended).
*   Write, save, and run a simple Python program ("Hello, World!").
*   Understand what comments are and how to use them.
*   Recognize a basic Python error message.

----------------------------------------------------

What is Programming?
====================

Think of programming as giving a set of very specific instructions to a computer. Computers are powerful, but they are also very literal. They will do *exactly* what you tell them to do, no more, no less.

A **program** is a sequence of these instructions, written in a language the computer can understand (or be translated into one). We, as programmers, write these instructions to solve problems, automate tasks, create games, build websites, analyze data, and much more!

.. tip::
   Analogy: Imagine you're giving instructions to a robot chef to make a sandwich. You can't just say "make me a sandwich." You need to specify:
   1. Take two slices of bread.
   2. Open the peanut butter jar.
   3. Spread peanut butter on one slice.
   4. ...and so on.
   Programming is similar – breaking down a task into small, precise steps.

----------------------------------------------------

Why Python?
===========

There are many programming languages, so why start with Python?

*   **Readability:** Python's syntax (the rules of how you write it) is designed to be clear and easy to read, almost like plain English. This makes it great for beginners.
*   **Versatility:** Python is a general-purpose language. You can use it for:
    *   Web development (like Instagram, YouTube, Spotify)
    *   Data science and machine learning
    *   Automation and scripting
    *   Scientific computing
    *   Game development
    *   And much more!
*   **Large Community & Libraries:** Python has a massive, active community. This means lots of help available online and a vast collection of pre-written code (called libraries or packages) that you can use to do complex things easily.
*   **Beginner-Friendly:** It has a gentle learning curve, allowing you to build cool things relatively quickly, which is very motivating!
*   **High Demand:** Python developers are in high demand in the job market.

----------------------------------------------------

Setting Up Your Environment
===========================

To start writing and running Python code, you need two main things:

1.  **The Python Interpreter:** This is the program that understands and executes your Python code.
2.  **A Code Editor:** This is a specialized text editor where you'll write your Python code files (scripts).

Installing Python
-----------------

1.  **Go to the Official Website:** The best place to get Python is from its official website: `python.org <https://www.python.org/downloads/>`_
2.  **Download the Installer:** Download the latest stable version for your operating system (Windows, macOS, Linux).
3.  **Run the Installer:**
    *   **Windows:** Make sure to check the box that says "Add Python to PATH" during installation. This is important!
    *   **macOS:** Python might already be pre-installed (an older version). It's generally recommended to install the latest version from python.org. The installer works like most macOS application installers.
    *   **Linux:** Python is usually pre-installed. You can check with `python3 --version`. If you need to install or update, use your distribution's package manager (e.g., `sudo apt-get install python3` on Debian/Ubuntu).
4.  **Verify Installation:** Open a terminal (Command Prompt or PowerShell on Windows, Terminal on macOS/Linux) and type:
    .. code-block:: bash

        python --version
        # or, on some systems, you might need:
        # python3 --version

    You should see the Python version number printed, e.g., `Python 3.10.4`. If you get an error, Python might not be installed correctly or not added to your system's PATH.

.. note::
   If you encounter issues with installation, a quick web search like "install python 3 on [Your OS]" often provides detailed, OS-specific guides and troubleshooting.

Choosing and Setting Up a Code Editor
---------------------------------------

While you *could* write Python code in a simple text editor like Notepad, a dedicated code editor offers many helpful features like syntax highlighting (coloring your code to make it easier to read), auto-completion, and debugging tools.

We recommend **Visual Studio Code (VS Code)**:

1.  **Download VS Code:** Get it from `code.visualstudio.com <https://code.visualstudio.com/>`_
2.  **Install it:** Follow the installation instructions for your OS.
3.  **Install the Python Extension:**
    *   Open VS Code.
    *   Go to the Extensions view (click the square icon on the sidebar or press ``Ctrl+Shift+X``).
    *   Search for "Python" (by Microsoft).
    *   Click "Install". This extension provides rich support for Python development.

.. tip::
    Take a few minutes to familiarize yourself with VS Code:
    *   The **Explorer** (sidebar) to open files and folders.
    *   The **Editor** area where you'll type code.
    *   The **Integrated Terminal** (you can open it via `Terminal > New Terminal` or ``Ctrl+` ``) where you'll run your Python scripts.

The Python Interpreter: Interactive vs. Script Mode
-----------------------------------------------------

You can interact with Python in two main ways:

1.  **Interactive Mode (REPL):**
    *   REPL stands for Read-Evaluate-Print Loop.
    *   You type Python commands one at a time, and Python executes them immediately and shows the result.
    *   To start it, open your terminal and type `python` or `python3`. You'll see a `>>>` prompt.
    *   Example:
        .. code-block:: pycon

            >>> print("Hello from interactive mode!")
            Hello from interactive mode!
            >>> 2 + 2
            4
            >>> exit()

    *   It's great for testing small snippets of code or exploring.

2.  **Script Mode:**
    *   You write your Python code in a file (usually with a `.py` extension, e.g., `my_program.py`).
    *   You then tell the Python interpreter to run all the instructions in that file from top to bottom.
    *   This is how you'll build larger applications.

----------------------------------------------------

Your First Python Program: "Hello, World!"
==========================================

It's a tradition in programming to make your first program display the text "Hello, World!". Let's do it.

1.  **Create a Folder:** Create a folder on your computer for your Python projects (e.g., `python_course`).
2.  **Open VS Code in this Folder:**
    *   In VS Code, go to `File > Open Folder...` and select the folder you created.
3.  **Create a New File:**
    *   In VS Code's Explorer, click the "New File" icon (or `File > New File`).
    *   Name the file `hello.py`. Make sure it ends with `.py`.
4.  **Write the Code:** Type the following line into `hello.py`:
    .. code-block:: python

        print("Hello, World!")

5.  **Save the File:** Press ``Ctrl+S`` (Windows/Linux) or ``Cmd+S`` (macOS).
6.  **Run the Program:**
    *   Open the integrated terminal in VS Code (`Terminal > New Terminal`).
    *   Make sure your terminal is in the correct directory (where `hello.py` is saved). If you opened the folder in VS Code, it usually is.
    *   Type the following command and press Enter:
        .. code-block:: bash

            python hello.py
            # or if that doesn't work, try:
            # python3 hello.py

7.  **See the Output:** You should see `Hello, World!` printed in the terminal.

.. image:: /_static/images/hello_world_output.png
   :alt: Terminal showing 'Hello, World!' output
   :width: 400px
   :align: center

   (Imagine a screenshot of a terminal showing the command and output)

**Congratulations! You've written and run your first Python program!** This is a significant first step.

----------------------------------------------------

Understanding Basic Errors
==========================

Errors are a normal part of programming. Don't be afraid of them! Python will try to tell you what went wrong.

Let's intentionally make an error. Change your `hello.py` to:

.. code-block:: python
    :emphasize-lines: 1

    print("Hello, World! # Missing closing parenthesis

If you try to run this, Python will give you a `SyntaxError`:

.. code-block:: text

    File "hello.py", line 1
      print("Hello, World!
            ^
    SyntaxError: unterminated string literal (detected at line 1)

Let's break down what this means:

*   `File "hello.py", line 1`: Tells you the error is in the file `hello.py` on line 1.
*   `print("Hello, World!`: Shows you the line where Python thinks the error is.
*   `^`: Points to where Python detected the problem.
*   `SyntaxError: unterminated string literal`: This is the type of error. A "string literal" is text in quotes. "Unterminated" means it wasn't properly closed.

Learning to read error messages is a crucial skill. They are your clues to fixing your code.

Fix the error by adding the closing parenthesis and quotation mark, then run it again to confirm it works.

----------------------------------------------------

Comments
========

Comments are notes in your code that are ignored by the Python interpreter. They are for humans – for you (to remember what your code does later) or for others (to understand your code).

In Python, anything on a line after a hash symbol (`#`) is a comment.

.. code-block:: python

    # This is a full-line comment.
    # It explains what the next line of code does.
    print("Hello, World!") # This is an end-of-line comment.

    # You can also use comments to temporarily "disable" code:
    # print("This line won't run.")
    print("This line will run.")

Good comments explain *why* you're doing something, or clarify complex parts of your code. Don't over-comment obvious things.

----------------------------------------------------

Mini-Project: Personalized Greeting
====================================

Time to practice!

**Goal:** Write a Python program that:
1.  Prints a personalized greeting to you.
2.  Prints a fun fact about Python (you can make one up or find one online).

**Example Output:**

.. code-block:: text

    Hello, [Your Name]! Welcome to the world of Python!
    Did you know? Python was named after Monty Python's Flying Circus!

**Steps:**

1.  Create a new file in VS Code (e.g., `greeting.py`).
2.  Write `print()` statements to achieve the goal.
3.  Use comments to explain what your program does.
4.  Save and run your program from the terminal.

.. admonition:: Solution (Try it yourself before looking!)
   :class: dropdown

   .. code-block:: python

       # greeting.py
       # This program prints a personalized greeting and a Python fun fact.

       # Print a personalized greeting
       print("Hello, Alex! Welcome to the world of Python!") # Replace Alex with your name

       # Print a fun fact about Python
       print("Did you know? Python is often used for cool things like AI and web apps!")

----------------------------------------------------

Module 0 Summary
================

Great job making it through Module 0! You've learned:

*   The basic concept of programming.
*   Why Python is a popular and useful language.
*   How to install Python and set up VS Code.
*   The thrill of running your first "Hello, World!" program.
*   How to understand basic errors and use comments.

You now have the foundational setup to dive deeper into Python. In the next module, we'll explore variables and different types of data you can work with.

Ready for more? Let's go to :ref:`module1-variables-and-data-types`!
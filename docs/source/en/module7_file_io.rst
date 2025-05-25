.. _module7-file-io:

============================================================
Module 7: File Input/Output - Interacting with Data Storage
============================================================

Welcome to Module 7! So far, our programs have worked with data that exists only while the program is running. Once the program ends, any data generated or modified is lost. To make data persistent—meaning it remains available even after the program finishes—we need to store it in **files**. **File Input/Output (I/O)** is the process of reading data from and writing data to files on a storage device (like a hard drive). This allows your programs to save their state, process large datasets, and interact with other programs.

.. image:: ../_static/images/file_io_concept.png
   :alt: A computer reading from and writing to a file document
   :width: 650px
   :align: center

Learning Objectives
-------------------

By the end of this module, you will be able to:

*   Understand the importance of file I/O for data persistence.
*   Open files in different modes (read, write, append, etc.) using the `open()` function.
*   Understand the importance of closing files and how to use the `with` statement for automatic resource management.
*   Read data from text files using methods like `read()`, `readline()`, and `readlines()`.
*   Iterate over file contents line by line.
*   Write data to text files using `write()` and `writelines()`.
*   Understand the difference between overwriting and appending to files.
*   Handle common file-related exceptions like `FileNotFoundError` and `PermissionError`.
*   Briefly understand how file paths work and use basic `os.path` functions.
*   Get a glimpse into working with structured file formats like CSV and JSON (though detailed exploration will be later).

----------------------------------------------------

What is File I/O?
=================

**File Input/Output (I/O)** refers to the operations that allow a program to read data from a file (input) or write data to a file (output). Files are stored on secondary storage devices (hard drives, SSDs, USB drives, etc.) and provide a way to persist data beyond the execution lifetime of a single program.

Types of Files
--------------
Broadly, files can be categorized into:

1.  **Text Files:**
    *   Store data as human-readable sequences of characters (text).
    *   Examples: `.txt`, `.py` (Python scripts), `.html`, `.csv`.
    *   Each line typically ends with a newline character (`\n`).
    *   Python handles encoding and decoding of characters automatically in most cases (UTF-8 is a common default).

2.  **Binary Files:**
    *   Store data as raw sequences of bytes, exactly as they are in computer memory.
    *   Not directly human-readable with a simple text editor.
    *   Examples: `.jpg` (images), `.mp3` (audio), `.exe` (executables), compiled code, database files.
    *   Require specific knowledge of the file format to interpret correctly.

This module will primarily focus on **text files**, as they are common and easier to get started with.

----------------------------------------------------

Opening and Closing Files
=========================

Before you can read from or write to a file, you must first **open** it. Python's built-in `open()` function is used for this.

The `open()` Function
---------------------
Syntax: `file_object = open(filename, mode, encoding=None)`

*   `filename`: A string representing the name (and path) of the file.
*   `mode`: A string specifying how the file should be opened. This is crucial.
*   `encoding` (optional): Specifies the encoding to be used for text files (e.g., `"utf-8"`, `"ascii"`). It's good practice to specify `utf-8` for broader compatibility, though Python might default to it depending on your system.

Common File Modes:
------------------
*   `'r'`: **Read mode (default).** Opens the file for reading. Raises an error if the file does not exist.
*   `'w'`: **Write mode.** Opens the file for writing.
    *   If the file exists, its contents are **truncated (erased)**.
    *   If the file does not exist, it is **created**.
*   `'a'`: **Append mode.** Opens the file for writing.
    *   Data is added to the **end of the file** if it exists.
    *   If the file does not exist, it is **created**.
*   `'x'`: **Exclusive creation mode.** Creates a new file and opens it for writing. Raises an error if the file already exists.
*   `'b'`: **Binary mode.** Can be added to other modes (e.g., `'rb'`, `'wb'`). Treats the file as a binary file.
*   `'+'`: **Update mode (read and write).** Can be added to other modes (e.g., `'r+'`, `'w+'`, `'a+'`).

Example:
.. code-block:: python

    # Open a file for reading
    # f = open("myfile.txt", "r")

    # Open a file for writing (creates if not exists, truncates if exists)
    # f = open("output.txt", "w")

    # Open a file for appending
    # f = open("log.txt", "a")

Closing Files: `file_object.close()`
------------------------------------
After you are done working with a file, it's very important to **close** it using the `close()` method of the file object.

.. code-block:: python

    file = open("example.txt", "w")
    # ... perform operations on the file ...
    file.write("Hello from Python!\n")
    file.close() # Essential to ensure data is written and resources are freed

Why close files?
*   **Data Buffering:** When you write to a file, data might be temporarily stored in a buffer. Closing the file ensures that all data in the buffer is written to the disk (flushed).
*   **Resource Management:** Operating systems have a limit on the number of files a program can have open simultaneously. Closing files frees up these resources.
*   **File Locking:** On some systems, an open file might be locked, preventing other programs (or even other parts of your program) from accessing it.

The `with` Statement (Context Manager)
--------------------------------------
Forgetting to close files is a common source of bugs and resource leaks. Python provides a more elegant and safer way to handle files using the `with` statement, also known as a context manager.

The `with` statement automatically takes care of closing the file, even if errors occur within the block.

.. code-block:: python

    # Preferred way to open and work with files
    try:
        with open("myfile.txt", "w", encoding="utf-8") as f:
            f.write("This is a line.\n")
            f.write("Another line using the 'with' statement.\n")
            # No need to call f.close() explicitly.
            # It's automatically called when the 'with' block exits.
        print("Data written to myfile.txt")
    except IOError as e:
        print(f"An I/O error occurred: {e}")

This is the recommended way to work with files in Python.

----------------------------------------------------

Reading from Files
==================

Once a file is opened in read mode (e.g., `'r'` or `'r+'`), you can read its contents.

1.  `file.read(size=-1)`:
    *   Reads and returns a string containing up to `size` bytes/characters from the file.
    *   If `size` is omitted or negative, it reads and returns the entire content of the file.
    *   Be cautious with very large files, as `read()` without `size` will load the whole file into memory.

    .. code-block:: python

        try:
            with open("myfile.txt", "r", encoding="utf-8") as f:
                content = f.read()
                print("--- Entire Content ---")
                print(content)
        except FileNotFoundError:
            print("Error: myfile.txt not found.")
        except IOError as e:
            print(f"An I/O error occurred: {e}")

2.  `file.readline(size=-1)`:
    *   Reads and returns a single line from the file, including the newline character (`\n`) at the end.
    *   If `size` is specified, it reads at most `size` bytes/characters.
    *   Returns an empty string (`""`) if the end of the file (EOF) is reached.

    .. code-block:: python

        try:
            with open("myfile.txt", "r", encoding="utf-8") as f:
                print("--- Reading line by line ---")
                line1 = f.readline()
                print(f"Line 1: {line1.strip()}") # .strip() removes leading/trailing whitespace like \n
                line2 = f.readline()
                print(f"Line 2: {line2.strip()}")
        except FileNotFoundError:
            print("Error: myfile.txt not found.")

3.  `file.readlines()`:
    *   Reads all remaining lines from the file and returns them as a list of strings.
    *   Each string in the list includes the newline character (`\n`).
    *   Like `read()`, this can consume a lot of memory for large files.

    .. code-block:: python

        try:
            with open("myfile.txt", "r", encoding="utf-8") as f:
                lines = f.readlines()
                print("--- All lines as a list ---")
                for i, line in enumerate(lines):
                    print(f"List Line {i}: {line.strip()}")
        except FileNotFoundError:
            print("Error: myfile.txt not found.")

4.  Iterating Over a File Object:
    This is the most memory-efficient way to read a file line by line, especially for large files, as it doesn't load the entire file into memory at once.

    .. code-block:: python

        try:
            with open("myfile.txt", "r", encoding="utf-8") as f:
                print("--- Iterating over the file ---")
                for line_number, current_line in enumerate(f):
                    # current_line includes the newline character
                    print(f"Iterated Line {line_number}: {current_line.strip()}")
        except FileNotFoundError:
            print("Error: myfile.txt not found.")

----------------------------------------------------

Writing to Files
================

To write data to a file, you need to open it in a write mode (`'w'`, `'a'`, `'x'`) or an update mode (`'+'`).

1.  `file.write(string)`:
    *   Writes the given `string` to the file.
    *   It does **not** automatically add a newline character. You must include `\n` if you want new lines.
    *   Returns the number of characters written.

    .. code-block:: python

        try:
            with open("output.txt", "w", encoding="utf-8") as f: # 'w' overwrites or creates
                f.write("Hello, file world!\n")
                f.write("This is the second line.\n")
                num_chars = f.write("Python is fun.")
                print(f"Wrote {num_chars} characters in the last write.")
            print("Data written to output.txt")

            with open("output.txt", "a", encoding="utf-8") as f: # 'a' appends
                f.write("\nThis line is appended.")
            print("Data appended to output.txt")
        except IOError as e:
            print(f"An I/O error occurred: {e}")

2.  `file.writelines(list_of_strings)`:
    *   Writes a list (or any iterable) of strings to the file.
    *   Like `write()`, it does **not** add newline characters between strings. You need to ensure your strings in the list already have them if desired.

    .. code-block:: python

        lines_to_write = [
            "First line for writelines.\n",
            "Second line.\n",
            "And a third one.\n"
        ]
        try:
            with open("writelines_example.txt", "w", encoding="utf-8") as f:
                f.writelines(lines_to_write)
            print("Data written using writelines() to writelines_example.txt")
        except IOError as e:
            print(f"An I/O error occurred: {e}")

Overwriting vs. Appending:
--------------------------
*   **`'w'` (Write mode):** If the file exists, its content is completely erased before new data is written. If it doesn't exist, it's created. Use this when you want to start fresh.
*   **`'a'` (Append mode):** If the file exists, new data is added to the end of the existing content. If it doesn't exist, it's created. Use this for logging or adding to existing data.

----------------------------------------------------

Working with File Paths
=======================

A **file path** specifies the location of a file or directory in a file system.

*   **Absolute Path:** Specifies the location from the root of the file system (e.g., `C:\Users\YourName\Documents\file.txt` on Windows, or `/home/yourname/documents/file.txt` on Linux/macOS).
*   **Relative Path:** Specifies the location relative to the current working directory of your script (e.g., `data/file.txt` or `../images/pic.jpg`).

The `os` Module
---------------
Python's `os` module provides functions for interacting with the operating system, including path manipulations. The `os.path` submodule is particularly useful.

.. code-block:: python

    import os

    # Get current working directory
    cwd = os.getcwd()
    print(f"Current Working Directory: {cwd}")

    # Construct a path in an OS-independent way
    filename = "my_notes.txt"
    filepath = os.path.join(cwd, "notes_folder", filename) # Good practice!
    print(f"Constructed Filepath: {filepath}")

    # Check if a file or directory exists
    if os.path.exists(filepath):
        print(f"'{filepath}' exists.")
    else:
        print(f"'{filepath}' does not exist.")
        # You might want to create the directory if it doesn't exist
        # os.makedirs(os.path.dirname(filepath), exist_ok=True) # Creates parent directories if needed

    # Get the directory part of a path
    dir_name = os.path.dirname(filepath)
    print(f"Directory part: {dir_name}")

    # Get the base name (file or last directory)
    base_name = os.path.basename(filepath)
    print(f"Base name: {base_name}")

The `pathlib` Module (Modern Alternative)
-----------------------------------------
Python 3.4+ introduced the `pathlib` module, which offers an object-oriented approach to file paths. It's often considered more convenient and Pythonic.

.. code-block:: python

    from pathlib import Path

    # Current working directory
    cwd_path = Path.cwd()
    print(f"Current Path (pathlib): {cwd_path}")

    # Constructing paths using / operator
    file_p = cwd_path / "notes_folder" / "my_notes.txt"
    print(f"Constructed Path (pathlib): {file_p}")

    # Check existence
    if file_p.exists():
        print(f"'{file_p}' exists (pathlib).")
    else:
        print(f"'{file_p}' does not exist (pathlib).")
        # Create parent directories if they don't exist when writing
        # file_p.parent.mkdir(parents=True, exist_ok=True)


    # Get parts of the path
    print(f"Parent directory (pathlib): {file_p.parent}")
    print(f"Filename (pathlib): {file_p.name}")
    print(f"File stem (name without suffix) (pathlib): {file_p.stem}")
    print(f"File suffix (extension) (pathlib): {file_p.suffix}")

    # Reading text (pathlib simplifies simple reads/writes)
    # try:
    #    content = file_p.read_text(encoding="utf-8")
    #    print(content)
    # except FileNotFoundError:
    #    print(f"{file_p} not found.")

    # Writing text
    # try:
    #    file_p.parent.mkdir(parents=True, exist_ok=True) # Ensure directory exists
    #    file_p.write_text("Hello from pathlib!", encoding="utf-8")
    #    print(f"Written to {file_p}")
    # except IOError as e:
    #    print(f"Error writing with pathlib: {e}")

For this module, basic `open()` with string paths is fine, but `pathlib` is good to be aware of for more complex path management.

----------------------------------------------------

Error Handling in File Operations
=================================

File operations are prone to errors. For example:
*   `FileNotFoundError`: Occurs if you try to open a file in read mode (`'r'`) that doesn't exist.
*   `PermissionError`: Occurs if you don't have the necessary permissions to read from or write to a file/directory.
*   `IsADirectoryError` / `NotADirectoryError`: Trying to treat a directory as a file or vice-versa.
*   `IOError`: A general I/O error (can be a base class for others like `FileNotFoundError`).

Always wrap file operations in `try...except` blocks.

.. code-block:: python

    file_to_read = "non_existent_file.txt"
    try:
        with open(file_to_read, "r", encoding="utf-8") as f:
            data = f.read()
            print(data)
    except FileNotFoundError:
        print(f"Error: The file '{file_to_read}' was not found.")
    except PermissionError:
        print(f"Error: You do not have permission to read '{file_to_read}'.")
    except IOError as e: # Catches other I/O related errors
        print(f"An I/O error occurred: {e}")
    except Exception as e: # Catch any other unexpected error
        print(f"An unexpected error occurred: {e}")

----------------------------------------------------

Brief Introduction to Structured File Formats
=============================================

While this module focuses on plain text files, many applications use structured file formats to store data in a more organized way. Two very common ones are:

1.  **CSV (Comma-Separated Values):**
    *   A text file format where data is stored in a tabular form.
    *   Each line represents a row, and values within a row are separated by commas (or other delimiters like tabs or semicolons).
    *   Python's `csv` module helps read and write CSV files easily.

    Example `data.csv`:
    ```csv
    Name,Age,City
    Alice,30,New York
    Bob,24,Paris
    Charlie,35,London
    ```

2.  **JSON (JavaScript Object Notation):**
    *   A lightweight text-based data interchange format.
    *   Human-readable and easy for machines to parse and generate.
    *   Uses a structure similar to Python dictionaries (key-value pairs) and lists.
    *   Python's `json` module is used for encoding Python objects into JSON strings/files and decoding JSON back into Python objects.

    Example `data.json`:
    ```json
    {
      "name": "Alice",
      "age": 30,
      "city": "New York",
      "isStudent": false,
      "courses": [
        {"title": "History", "credits": 3},
        {"title": "Math", "credits": 4}
      ]
    }
    ```

We will explore these formats in more detail in later modules or advanced topics. For now, understanding basic text file I/O is the foundation.

----------------------------------------------------

Mini-Project: Simple To-Do List Manager
=======================================

Let's create a command-line to-do list manager that saves tasks to a text file (`todo.txt`). Each task will be on a new line.

**Features:**
1.  **Add a task:** Prompts the user for a task and adds it to `todo.txt`.
2.  **View tasks:** Reads `todo.txt` and displays all tasks with numbers.
3.  **Remove a task:** Shows tasks with numbers, asks the user which one to remove, and updates `todo.txt`.
4.  **Exit:** Saves any changes and exits the program.
5.  The program should load existing tasks from `todo.txt` when it starts.

**File Structure (`todo.txt`):**
```
Buy groceries
Pay bills
Call mom
```

**Steps:**

1.  **`load_tasks(filename)` function:**
    *   Takes `filename` as input.
    *   Tries to open and read tasks from the file. Each line is a task.
    *   Returns a list of tasks.
    *   If the file doesn't exist, it should return an empty list (and perhaps print a message that a new file will be created). Handle `FileNotFoundError`.
2.  **`save_tasks(filename, tasks)` function:**
    *   Takes `filename` and a `list` of `tasks` as input.
    *   Opens the file in write mode (`'w'`) and writes each task to a new line. Handle potential `IOError`.
3.  **`add_task(tasks, description)` function:**
    *   Appends the `description` to the `tasks` list.
4.  **`view_tasks(tasks)` function:**
    *   If `tasks` is empty, prints "No tasks in the list."
    *   Otherwise, prints tasks with 1-based numbering.
5.  **`remove_task(tasks, task_number)` function:**
    *   Takes the `tasks` list and a 1-based `task_number` to remove.
    *   Validates `task_number`. If valid, removes the task. If invalid, prints an error.
6.  **Main Program Loop (`main` function):**
    *   Define `TODO_FILENAME = "todo.txt"`.
    *   Load tasks using `load_tasks()`.
    *   Use a `while True` loop to display a menu:
        ```
        To-Do List Manager
        1. Add Task
        2. View Tasks
        3. Remove Task
        4. Exit
        Enter your choice:
        ```
    *   Based on user choice, call the appropriate functions.
    *   For "Add", get task description.
    *   For "Remove", first view tasks, then get task number.
    *   For "Exit", call `save_tasks()` and `break` the loop.
    *   Include basic input validation and error messages.

**Example Interaction:**
.. code-block:: text
    To-Do List Manager
    1. Add Task
    2. View Tasks
    3. Remove Task
    4. Exit
    Enter your choice: 2
    Current Tasks:
    1. Buy groceries
    2. Pay bills
    ---
    Enter your choice: 1
    Enter task description: Walk the dog
    Task added.
    ---
    Enter your choice: 2
    Current Tasks:
    1. Buy groceries
    2. Pay bills
    3. Walk the dog
    ---
    Enter your choice: 3
    Current Tasks:
    1. Buy groceries
    2. Pay bills
    3. Walk the dog
    Enter task number to remove: 2
    Task "Pay bills" removed.
    ---
    Enter your choice: 4
    Tasks saved. Exiting.

.. admonition:: Solution (Try it yourself before looking!)
   :class: dropdown

   .. code-block:: python

       # todo_manager.py
       import os

       TODO_FILENAME = "todo.txt"

       def load_tasks(filename=TODO_FILENAME):
           """Loads tasks from the specified file."""
           tasks = []
           try:
               with open(filename, "r", encoding="utf-8") as f:
                   for line in f:
                       tasks.append(line.strip()) # Remove newline characters
               print(f"Tasks loaded from {filename}.")
           except FileNotFoundError:
               print(f"'{filename}' not found. Starting with an empty list.")
           except IOError as e:
               print(f"Error loading tasks from '{filename}': {e}")
           return tasks

       def save_tasks(tasks, filename=TODO_FILENAME):
           """Saves the list of tasks to the specified file."""
           try:
               with open(filename, "w", encoding="utf-8") as f:
                   for task in tasks:
                       f.write(task + "\n")
               print(f"Tasks saved to {filename}.")
           except IOError as e:
               print(f"Error saving tasks to '{filename}': {e}")

       def add_task_to_list(tasks_list, description):
           """Adds a new task to the list."""
           if description:
               tasks_list.append(description)
               print(f"Task '{description}' added.")
           else:
               print("Task description cannot be empty.")

       def view_tasks_in_list(tasks_list):
           """Displays all tasks in the list with numbering."""
           if not tasks_list:
               print("No tasks in the list.")
               return

           print("\nCurrent Tasks:")
           print("-" * 15)
           for i, task in enumerate(tasks_list):
               print(f"{i + 1}. {task}")
           print("-" * 15)

       def remove_task_from_list(tasks_list):
           """Removes a task from the list based on its number."""
           if not tasks_list:
               print("No tasks to remove.")
               return False # Indicate no removal happened

           view_tasks_in_list(tasks_list)
           try:
               task_num_str = input("Enter the number of the task to remove: ")
               task_num = int(task_num_str)

               if 1 <= task_num <= len(tasks_list):
                   removed_task = tasks_list.pop(task_num - 1) # Adjust for 0-based index
                   print(f"Task '{removed_task}' removed.")
                   return True # Indicate successful removal
               else:
                   print("Invalid task number.")
           except ValueError:
               print("Invalid input. Please enter a number.")
           return False # Indicate no removal or failed attempt

       def print_menu():
           """Prints the main menu options."""
           print("\nTo-Do List Manager")
           print("--------------------")
           print("1. Add Task")
           print("2. View Tasks")
           print("3. Remove Task")
           print("4. Save and Exit")
           print("5. Exit Without Saving")


       def main():
           """Main function to run the To-Do List application."""
           tasks = load_tasks()
           made_changes = False

           while True:
               print_menu()
               choice = input("Enter your choice (1-5): ")

               if choice == '1':
                   description = input("Enter task description: ").strip()
                   add_task_to_list(tasks, description)
                   made_changes = True
               elif choice == '2':
                   view_tasks_in_list(tasks)
               elif choice == '3':
                   if remove_task_from_list(tasks):
                       made_changes = True
               elif choice == '4':
                   save_tasks(tasks)
                   print("Exiting To-Do List Manager.")
                   break
               elif choice == '5':
                   if made_changes:
                       confirm = input("You have unsaved changes. Are you sure you want to exit without saving? (yes/no): ").lower()
                       if confirm == 'yes':
                           print("Exiting To-Do List Manager without saving.")
                           break
                   else:
                       print("Exiting To-Do List Manager.")
                       break
               else:
                   print("Invalid choice. Please enter a number between 1 and 5.")

       if __name__ == "__main__":
           main()

----------------------------------------------------

Module 7 Summary
================

Excellent work on completing Module 7! You've now gained essential skills for making your Python programs interact with the file system, allowing for data persistence and more complex applications. You've learned:

*   The fundamentals of **File I/O** and the difference between text and binary files.
*   How to **open files** using `open()` with various modes (`'r'`, `'w'`, `'a'`, etc.).
*   The critical importance of **closing files** and the convenience of using the `with` statement for automatic management.
*   Various methods for **reading from files** (`read()`, `readline()`, `readlines()`, and iteration).
*   How to **write to files** (`write()`, `writelines()`) and understand appending vs. overwriting.
*   Basic **file path manipulation** using `os.path` (and a glimpse of `pathlib`).
*   To anticipate and handle common **file-related exceptions** like `FileNotFoundError`.
*   A brief introduction to structured file formats like **CSV and JSON**, setting the stage for future learning.

Being able to read from and write to files is a fundamental skill that opens up a vast range of possibilities, from simple data logging to complex data processing applications.

Next up, we'll explore how to further organize your Python code into reusable units and leverage code written by others: :ref:`module8-modules-packages`!

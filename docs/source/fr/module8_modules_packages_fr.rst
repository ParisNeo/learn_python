.. _module8-modules-packages-fr:

================================================================
Module 8 : Modules et Paquets - Organiser Votre Code
================================================================

Bienvenue dans le Module 8 ! À mesure que vos projets Python gagnent en taille et en complexité, conserver tout votre code dans un seul fichier devient peu pratique et difficile à gérer. Les **modules** et les **paquets (packages)** sont la manière dont Python vous aide à organiser votre code en unités logiques et réutilisables. Un module est essentiellement un fichier Python contenant des définitions et des instructions (fonctions, classes, variables). Un paquet est une collection de modules apparentés organisés dans une hiérarchie de répertoires. L'utilisation de modules et de paquets favorise la réutilisabilité du code, la maintenabilité et la collaboration.

.. image:: ../_static/images/modules_packages_library.png
   :alt: Une étagère de bibliothèque représentant les modules et les paquets
   :width: 650px
   :align: center

Objectifs d'Apprentissage
-------------------

À la fin de ce module, vous serez capable de :

*   Comprendre ce que sont les modules et pourquoi ils sont utilisés.
*   Créer vos propres modules Python.
*   Importer des modules et leurs composants en utilisant les instructions `import` et `from ... import`.
*   Utiliser des alias pour les modules ou composants importés.
*   Comprendre le concept de la Bibliothèque Standard Python et utiliser certains de ses modules courants (par ex., `math`, `random`, `datetime`, `os`).
*   Comprendre ce que sont les paquets et comment ils organisent les modules.
*   Créer une structure de paquet simple.
*   Comprendre le rôle de `__init__.py` dans les paquets.
*   Comprendre brièvement comment trouver et installer des paquets tiers en utilisant `pip`.

----------------------------------------------------

Qu'est-ce qu'un Module ?
========================

Un **module** en Python est simplement un fichier avec une extension `.py` qui contient des définitions et des instructions Python. Ces définitions peuvent inclure des fonctions, des classes et des variables. Les modules vous permettent d'organiser logiquement votre code Python. Regrouper du code apparenté dans un module rend le code plus facile à comprendre, à utiliser et à maintenir.

Pourquoi Utiliser des Modules ?
-----------------------------
*   **Organisation :** Diviser les grands programmes en fichiers plus petits, gérables et organisés.
*   **Réutilisabilité :** Définir des fonctions ou des classes dans un module une seule fois et les utiliser dans plusieurs parties de votre programme ou dans différents programmes.
*   **Isolation des Espaces de Noms (Namespace) :** Les modules créent des espaces de noms séparés, ce qui aide à éviter les conflits de noms entre les identifiants (variables, fonctions, etc.) dans différentes parties de votre code.
*   **Collaboration :** Différents développeurs peuvent travailler simultanément sur différents modules.

Pensez aux fichiers Python que vous avez créés jusqu'à présent – chacun peut être considéré comme un module !

----------------------------------------------------

Création et Utilisation des Modules
===================================

Creating a Module
-----------------
Creating a module is as simple as saving your Python code in a file with a `.py` extension.

Let's create a simple module named `mymath.py`:

.. code-block:: python
    # mymath.py

    """A simple module for basic math operations."""

    PI = 3.14159

    def add(x, y):
        """Returns the sum of x and y."""
        return x + y

    def subtract(x, y):
        """Returns the difference of x and y."""
        return x - y

    def multiply(x, y):
        """Returns the product of x and y."""
        return x * y

    def divide(x, y):
        """Returns the division of x by y. Handles division by zero."""
        if y == 0:
            return "Error: Cannot divide by zero"
        return x / y

This `mymath.py` file is now a module.

Importing a Module
------------------
To use the definitions (functions, variables) from a module in another Python script or in the interactive interpreter, you need to **import** it. The `import` statement is used for this.

**1. `import module_name`**
This imports the entire module. To access its contents, you need to use the module name as a prefix (dot notation: `module_name.member_name`).

Create another file, say `main_program.py`, in the **same directory** as `mymath.py`:

.. code-block:: python
    # main_program.py

    import mymath # Imports the entire mymath.py module

    result_add = mymath.add(10, 5)
    print(f"Addition: {result_add}") # Output: Addition: 15

    result_subtract = mymath.subtract(10, 5)
    print(f"Subtraction: {result_subtract}") # Output: Subtraction: 5

    print(f"Value of PI from mymath: {mymath.PI}") # Output: Value of PI from mymath: 3.14159

    result_div = mymath.divide(10, 0)
    print(f"Division: {result_div}") # Output: Division: Error: Cannot divide by zero

**2. `from module_name import member1, member2, ...`**
This imports specific members (functions, variables, classes) from a module directly into the current namespace. You can then use them without the module name prefix.

.. code-block:: python
    # main_program_from.py

    from mymath import add, PI # Imports only add function and PI variable

    result_add = add(20, 7) # No mymath. prefix needed
    print(f"Addition (using 'from'): {result_add}") # Output: Addition (using 'from'): 27

    print(f"Value of PI (using 'from'): {PI}") # Output: Value of PI (using 'from'): 3.14159

    # subtract(10, 2) # This would cause a NameError because subtract was not imported

**3. `from module_name import *` (Wildcard Import)**
This imports all names (except those starting with an underscore `_`) from a module into the current namespace.
**Caution:** This is generally discouraged for larger programs because it can lead to namespace pollution and make it unclear where a particular function or variable came from, potentially causing naming conflicts.

.. code-block:: python
    # main_program_from_all.py

    from mymath import * # Imports all public names from mymath

    result_mult = multiply(6, 7)
    print(f"Multiplication: {result_mult}") # Output: Multiplication: 42
    print(f"PI again: {PI}")

Importing with an Alias
-----------------------
You can import a module or its members with an alias (an alternative name) using the `as` keyword. This is useful if the original module name is long or if you want to avoid naming conflicts.

.. code-block:: python
    # main_program_alias.py

    import mymath as mm # Import mymath module with alias 'mm'
    from mymath import divide as div_func # Import divide function with alias 'div_func'

    sum_val = mm.add(100, 50)
    print(f"Sum using alias: {sum_val}") # Output: Sum using alias: 150

    quotient = div_func(10, 2)
    print(f"Quotient using alias: {quotient}") # Output: Quotient using alias: 5.0

Module Search Path
------------------
When you use `import mymodule`, Python searches for `mymodule.py` in a list of directories:
1.  The directory containing the input script (or the current directory if interactive).
2.  `PYTHONPATH` (a list of directory names, with the same syntax as the shell variable `PATH`).
3.  The installation-dependent default path (usually includes the site-packages directory where third-party libraries are installed).

You can see the search path by inspecting `sys.path`:
.. code-block:: python
    import sys
    # print(sys.path)

The `if __name__ == "__main__":` Block
--------------------------------------
You've seen this in some examples. It's a common idiom in Python modules.
*   Every module in Python has a special built-in variable called `__name__`.
*   When a module is run directly (e.g., `python mymodule.py`), its `__name__` is set to `"__main__"`.
*   When a module is imported into another module, its `__name__` is set to its own filename (without `.py`).

This allows you to write code in a module that will only execute when the module is run as the main program, but not when it's imported by another module. This is often used for tests or to provide a command-line interface for the module.

Modify `mymath.py`:
.. code-block:: python
    # mymath.py (updated)

    """A simple module for basic math operations."""

    PI = 3.14159

    def add(x, y):
        """Returns the sum of x and y."""
        return x + y

    # ... (subtract, multiply, divide functions as before) ...
    def subtract(x, y): return x - y
    def multiply(x, y): return x * y
    def divide(x, y):
        if y == 0: return "Error: Cannot divide by zero"
        return x / y

    # This code runs only if mymath.py is executed directly
    if __name__ == "__main__":
        print("mymath.py is being run directly.")
        print(f"Testing add(2, 3): {add(2, 3)}")
        print(f"Testing divide(5, 0): {divide(5, 0)}")
        print(f"PI is: {PI}")

If you run `python mymath.py`, you'll see the test messages.
If you run `python main_program.py` (which imports `mymath`), you won't see those test messages from `mymath.py` because its `__name__` will be `"mymath"`.

----------------------------------------------------

La Bibliothèque Standard Python
================================

Python comes with a vast **Standard Library**, which is a collection of modules that provide a wide range of functionalities. You don't need to install these separately; they are part of your Python installation. Learning to use the Standard Library effectively is key to becoming a productive Python programmer.

Some Commonly Used Modules:
---------------------------

1.  **`math` Module:**
    Provides access to mathematical functions.

    .. code-block:: python
        import math

        print(f"Value of pi: {math.pi}")  # More precise pi
        print(f"Square root of 16: {math.sqrt(16)}") # Output: 4.0
        print(f"Ceiling of 4.3: {math.ceil(4.3)}")   # Output: 5
        print(f"Floor of 4.8: {math.floor(4.8)}")     # Output: 4
        print(f"Factorial of 5: {math.factorial(5)}") # Output: 120
        print(f"Sine of pi/2: {math.sin(math.pi / 2)}") # Output: 1.0

2.  **`random` Module:**
    For generating random numbers and making random choices.

    .. code-block:: python
        import random

        # Random float between 0.0 (inclusive) and 1.0 (exclusive)
        print(f"Random float: {random.random()}")

        # Random integer between a and b (inclusive)
        print(f"Random integer (1-10): {random.randint(1, 10)}")

        # Random choice from a sequence
        my_list = ['apple', 'banana', 'cherry', 'date']
        print(f"Random choice: {random.choice(my_list)}")

        # Shuffle a list in place
        random.shuffle(my_list)
        print(f"Shuffled list: {my_list}")

3.  **`datetime` Module:**
    For working with dates and times.

    .. code-block:: python
        import datetime

        # Current date and time
        now = datetime.datetime.now()
        print(f"Current date and time: {now}")

        # Current date
        today = datetime.date.today()
        print(f"Today's date: {today}")

        # Specific date
        d = datetime.date(2024, 7, 20)
        print(f"Specific date: {d}")

        # Formatting dates as strings
        print(f"Formatted date: {now.strftime('%Y-%m-%d %H:%M:%S')}") # YYYY-MM-DD HH:MM:SS
        print(f"Friendly date: {now.strftime('%A, %B %d, %Y')}")

4.  **`os` Module:**
    Provides functions for interacting with the operating system (file system operations, environment variables, etc.). We saw some of `os.path` in the File I/O module.

    .. code-block:: python
        import os

        print(f"Current working directory: {os.getcwd()}")
        # os.mkdir("new_directory") # Creates a new directory
        # print(f"Files in CWD: {os.listdir('.')}") # Lists files in current directory

        # For path manipulations, `os.path` is heavily used:
        print(f"Is 'mymath.py' a file? {os.path.isfile('mymath.py')}")
        print(f"Does 'my_folder' exist? {os.path.exists('my_folder')}")

5.  **`sys` Module:**
    Provides access to system-specific parameters and functions (command-line arguments, Python path, exit function).

    .. code-block:: python
        import sys

        print(f"Python version: {sys.version}")
        print(f"Command line arguments: {sys.argv}") # sys.argv[0] is the script name
        # sys.exit("Exiting program now!") # Terminates the program

6.  **`json` Module:**
    For working with JSON (JavaScript Object Notation) data.

    .. code-block:: python
        import json

        # Python dictionary
        data = {"name": "Alice", "age": 30, "city": "New York"}

        # Convert Python dict to JSON string
        json_string = json.dumps(data, indent=4) # dumps = dump string
        print("--- JSON String ---")
        print(json_string)

        # Convert JSON string back to Python dict
        parsed_data = json.loads(json_string) # loads = load string
        print(f"\nParsed name: {parsed_data['name']}")

        # To work with files:
        # with open('data.json', 'w') as f:
        #    json.dump(data, f, indent=4) # dump = dump to file object

        # with open('data.json', 'r') as f:
        #    loaded_from_file = json.load(f) # load = load from file object
        #    print(f"\nLoaded from file: {loaded_from_file}")

This is just a small sample. The Python Standard Library documentation is an excellent resource for exploring all available modules.

----------------------------------------------------

Paquets (Packages)
==================

As you develop more modules, you might want to organize them further. A **package** is a way of structuring Python's module namespace by using "dotted module names". A package is essentially a directory containing:
1.  One or more Python modules (`.py` files).
2.  A special file named `__init__.py` (can be empty). This file tells Python that the directory should be treated as a package.
3.  Optionally, sub-packages (subdirectories also containing an `__init__.py` file).

Example Package Structure:
--------------------------
Let's create a package named `mycompany_utils`.

```
myproject/
├── main_app.py
└── mycompany_utils/        <-- This is the package directory
    ├── __init__.py         <-- Makes 'mycompany_utils' a package
    ├── string_tools.py     <-- A module in the package
    └── math_tools.py       <-- Another module in the package
    └── network/            <-- A sub-package
        ├── __init__.py     <-- Makes 'network' a sub-package
        └── requester.py    <-- A module in the sub-package
```

**1. Create the directory structure:**
   Create the folders `myproject`, `mycompany_utils` inside `myproject`, and `network` inside `mycompany_utils`.

**2. Create `__init__.py` files:**
   Create an empty file named `__init__.py` inside `mycompany_utils/` and another empty one inside `mycompany_utils/network/`.
   *   `mycompany_utils/__init__.py`
   *   `mycompany_utils/network/__init__.py`

   The `__init__.py` files can also contain Python code. This code is executed when the package or a module within it is imported. It can be used to:
   *   Initialize package-level data.
   *   Specify which modules to import when `from package import *` is used (by defining `__all__`).
   *   Import submodules to make them available at the package level for convenience.

**3. Create modules within the package:**

   `mycompany_utils/string_tools.py`:
   .. code-block:: python
       # mycompany_utils/string_tools.py
       def reverse_string(s):
           return s[::-1]

       def count_vowels(s):
           vowels = "aeiouAEIOU"
           count = 0
           for char in s:
               if char in vowels:
                   count += 1
           return count

   `mycompany_utils/math_tools.py`: (You can reuse `mymath.py` content or make it simpler)
   .. code-block:: python
       # mycompany_utils/math_tools.py
       PI = 3.14159
       def power(base, exp):
           return base ** exp

   `mycompany_utils/network/requester.py`:
   .. code-block:: python
       # mycompany_utils/network/requester.py
       def fetch_data(url):
           print(f"Simulating fetching data from {url}...")
           return {"status": "success", "data": f"content from {url}"}

Importing from Packages
-----------------------
Now, from `main_app.py` (which is outside the `mycompany_utils` package, but in its parent directory `myproject`), you can import modules from the package:

`myproject/main_app.py`:
.. code-block:: python
    # myproject/main_app.py

    # Option 1: Import specific modules from the package
    import mycompany_utils.string_tools
    import mycompany_utils.math_tools
    from mycompany_utils.network import requester

    print("--- Option 1 ---")
    reversed_name = mycompany_utils.string_tools.reverse_string("Python")
    print(f"Reversed: {reversed_name}") # Output: Reversed: nohtyP

    two_cubed = mycompany_utils.math_tools.power(2, 3)
    print(f"2^3: {two_cubed}") # Output: 2^3: 8

    data = requester.fetch_data("http://example.com")
    print(f"Fetched: {data}") # Output: Fetched: {'status': 'success', 'data': 'content from http://example.com'}


    # Option 2: Import specific functions/variables using 'from'
    from mycompany_utils.string_tools import count_vowels
    from mycompany_utils.math_tools import PI
    # from mycompany_utils.network.requester import fetch_data # Already imported above

    print("\n--- Option 2 ---")
    vowel_count = count_vowels("Hello World")
    print(f"Vowels in 'Hello World': {vowel_count}") # Output: Vowels in 'Hello World': 3
    print(f"PI from math_tools: {PI}")


    # Option 3: Using aliases
    import mycompany_utils.string_tools as st
    from mycompany_utils.network import requester as req

    print("\n--- Option 3 ---")
    print(f"Reversed 'Test' using alias: {st.reverse_string('Test')}")
    req.fetch_data("http://anothersite.org")

Controlling Package Imports with `__init__.py`
----------------------------------------------
You can make parts of your package more easily accessible by importing them in the package's `__init__.py`.

Edit `mycompany_utils/__init__.py`:
.. code-block:: python
    # mycompany_utils/__init__.py

    print("mycompany_utils package is being initialized!")

    # Make functions from string_tools directly available from mycompany_utils
    from .string_tools import reverse_string, count_vowels

    # Make PI from math_tools available
    from .math_tools import PI

    # You can also import entire submodules or subpackages
    from . import math_tools
    from . import network

    # Define __all__ to control 'from mycompany_utils import *'
    __all__ = ['reverse_string', 'count_vowels', 'PI', 'math_tools', 'network']

Now, in `main_app.py`, you could potentially simplify imports (though explicit is often better):

.. code-block:: python
    # myproject/main_app.py (demonstrating effect of __init__.py)
    import mycompany_utils

    print("\n--- Using __init__.py conveniences ---")
    # Functions directly available due to __init__.py
    print(f"Reversed 'Example' by mycompany_utils: {mycompany_utils.reverse_string('Example')}")
    print(f"PI from mycompany_utils: {mycompany_utils.PI}")

    # Accessing a submodule imported in __init__.py
    print(f"3^3: {mycompany_utils.math_tools.power(3, 3)}")
    mycompany_utils.network.requester.fetch_data("http://init-test.com")

    # If you did 'from mycompany_utils import *', only names in __all__ would be imported.

Relative Imports within a Package
---------------------------------
When modules within the same package need to import each other, you can use relative imports using dot `.` notation.
*   `from . import sibling_module`
*   `from .sibling_module import something`
*   `from .. import parent_package_module` (imports from the parent package)
*   `from ..parent_package_module import something`

Example: If `mycompany_utils/math_tools.py` needed a function from `mycompany_utils/string_tools.py`:
```python
# In mycompany_utils/math_tools.py
# from .string_tools import some_string_function # Correct relative import
# import string_tools # This would be an absolute import, might fail or pick up wrong module
```

----------------------------------------------------

Paquets Tiers et `pip`
======================

The Python Standard Library is extensive, but it doesn't cover everything. The Python community has created a vast ecosystem of **third-party packages** that provide functionalities for almost any task imaginable (web development, data science, machine learning, image processing, etc.).

**PyPI (Python Package Index):**
PyPI (pypi.org) is the official repository for third-party Python software. You can find and download packages from here.

**`pip` (Package Installer for Python):**
`pip` is the standard package manager for Python. It's used to install and manage packages from PyPI and other sources. `pip` is usually included with modern Python installations.

Common `pip` Commands (run in your terminal/command prompt, not Python interpreter):
---------------------------------------------------------------------------------
*   **Install a package:**
    ```bash
    pip install package_name
    # Example:
    pip install requests  # A popular library for making HTTP requests
    pip install numpy     # For numerical computing
    pip install pandas    # For data analysis
    ```

*   **Install a specific version of a package:**
    ```bash
    pip install package_name==1.2.3
    ```

*   **Upgrade a package:**
    ```bash
    pip install --upgrade package_name
    ```

*   **Uninstall a package:**
    ```bash
    pip uninstall package_name
    ```

*   **List installed packages:**
    ```bash
    pip list
    ```

*   **Show information about an installed package:**
    ```bash
    pip show package_name
    ```

*   **Install packages from a requirements file:**
    It's common practice to list a project's dependencies in a file named `requirements.txt`.
    `requirements.txt` might look like:
    ```
    requests==2.25.1
    numpy>=1.20.0
    pandas
    ```
    Then, you can install all of them with:
    ```bash
    pip install -r requirements.txt
    ```

*   **Generate a `requirements.txt` from the current environment:**
    ```bash
    pip freeze > requirements.txt
    ```
    (This captures all packages; for project-specific dependencies, virtual environments are recommended).

Virtual Environments
--------------------
When working on multiple projects, they might have different, potentially conflicting, package dependencies. **Virtual environments** allow you to create isolated Python environments for each project. This means each project can have its own set of installed packages without affecting others or the global Python installation.

Common tools for virtual environments:
*   `venv` (built into Python 3.3+)
*   `virtualenv` (a third-party tool, was common before `venv`)
*   `conda` (popular in the data science community, manages environments and packages)

Using `venv` (brief example):
1.  **Create a virtual environment:**
    (Navigate to your project directory first)
    ```bash
    python -m venv myenv  # 'myenv' is the name of the environment directory
    ```
2.  **Activate the environment:**
    *   On Windows:
        ```bash
        myenv\Scripts\activate
        ```
    *   On macOS/Linux:
        ```bash
        source myenv/bin/activate
        ```
    Your terminal prompt will usually change to indicate the active environment.
3.  **Install packages:** `pip install ...` (these will be installed *inside* `myenv`)
4.  **Deactivate the environment:**
    ```bash
    deactivate
    ```

Using virtual environments is a highly recommended best practice for Python development.

----------------------------------------------------

Mini-Projet : Outil d'Analyse de Texte
======================================

Construisons un outil simple d'analyse de texte qui utilise des modules. Nous allons créer un paquet pour nos fonctions d'analyse.

**Project Structure:**
```
text_analyzer_project/
├── main_analyzer.py
└── textstats/
    ├── __init__.py
    ├── counter.py      # Module for counting words, characters, lines
    └── formatter.py    # Module for formatting output
```

**Goals:**
1.  **`textstats/counter.py` module:**
    *   `count_words(text_string)`: Returns the number of words in the string.
    *   `count_characters(text_string, include_spaces=True)`: Returns the number of characters.
    *   `count_lines(text_string)`: Returns the number of lines.
2.  **`textstats/formatter.py` module:**
    *   `format_report(word_count, char_count, line_count)`: Returns a nicely formatted string report.
3.  **`textstats/__init__.py`:**
    *   Make the core functions from `counter` and `formatter` easily accessible from the `textstats` package.
4.  **`main_analyzer.py`:**
    *   Prompts the user to enter some text or provide a filename to read.
    *   If a filename is given, read its content (handle `FileNotFoundError`).
    *   Uses the `textstats` package to analyze the text.
    *   Prints the formatted report.
    *   Uses at least one module from the Python Standard Library (e.g., `os.path.exists` or `sys` for arguments if you want to extend it).

**Example Interaction (if user types text):**
.. code-block:: text
    Enter text to analyze or a filename: Hello world. This is a test.
    Analyzing your text...

    --- Text Analysis Report ---
    Words: 6
    Characters (incl. spaces): 29
    Lines: 1
    --------------------------

**Example Interaction (if user provides filename):**
Create a `sample.txt` in `text_analyzer_project/`:
```
This is line one.
This is line two.
And a third line.
```
.. code-block:: text
    Enter text to analyze or a filename: sample.txt
    Reading from file: sample.txt
    Analyzing your text...

    --- Text Analysis Report ---
    Words: 12
    Characters (incl. spaces): 50
    Lines: 3
    --------------------------

.. admonition:: Solution (Essayez par vous-même avant de regarder !)
   :class: dropdown

   .. code-block:: python

       # text_analyzer_project/textstats/counter.py

       def count_words(text_string):
           """Counts the number of words in a string."""
           if not text_string:
               return 0
           words = text_string.split()
           return len(words)

       def count_characters(text_string, include_spaces=True):
           """Counts the number of characters in a string."""
           if not text_string:
               return 0
           if include_spaces:
               return len(text_string)
           else:
               return len(text_string.replace(" ", ""))

       def count_lines(text_string):
           """Counts the number of lines in a string."""
           if not text_string:
               return 0
           # splitlines() handles various newline characters correctly
           lines = text_string.splitlines()
           return len(lines) if lines else 1 # Handles single line without newline at end

       # Test block (optional)
       if __name__ == "__main__":
           sample_text = "Hello world.\nThis is a test."
           print(f"Words: {count_words(sample_text)}")
           print(f"Chars (incl spaces): {count_characters(sample_text)}")
           print(f"Chars (excl spaces): {count_characters(sample_text, include_spaces=False)}")
           print(f"Lines: {count_lines(sample_text)}")
           print(f"Lines in 'single': {count_lines('single')}")

   .. code-block:: python

       # text_analyzer_project/textstats/formatter.py

       def format_report(word_count, char_count, line_count, char_count_no_spaces=None):
           """Formats the analysis results into a string report."""
           report = "\n--- Text Analysis Report ---\n"
           report += f"Words: {word_count}\n"
           report += f"Characters (incl. spaces): {char_count}\n"
           if char_count_no_spaces is not None:
               report += f"Characters (excl. spaces): {char_count_no_spaces}\n"
           report += f"Lines: {line_count}\n"
           report += "--------------------------"
           return report

       if __name__ == "__main__":
           print(format_report(10, 50, 3, 40))

   .. code-block:: python

       # text_analyzer_project/textstats/__init__.py

       """
       TextStats Package
       Provides utilities for basic text analysis.
       """

       # Make key functions directly available from the textstats package
       from .counter import count_words, count_characters, count_lines
       from .formatter import format_report

       __all__ = ['count_words', 'count_characters', 'count_lines', 'format_report']

       print("TextStats package initialized.") # Just for demonstration

   .. code-block:: python

       # text_analyzer_project/main_analyzer.py
       import os
       import sys # Just to show another standard library import
       import textstats # Import our package

       def get_text_input():
           """Gets text from user input or a file."""
           user_input = input("Enter text to analyze or a filename: ").strip()

           if os.path.exists(user_input) and os.path.isfile(user_input):
               try:
                   print(f"Reading from file: {user_input}")
                   with open(user_input, "r", encoding="utf-8") as f:
                       return f.read()
               except FileNotFoundError: # Should be caught by os.path.exists, but good practice
                   print(f"Error: File '{user_input}' not found (should not happen here).")
                   return None
               except IOError as e:
                   print(f"Error reading file '{user_input}': {e}")
                   return None
               except Exception as e:
                   print(f"An unexpected error occurred while reading file: {e}")
                   return None
           elif not user_input:
               print("No input provided.")
               return None
           else:
               # Assume it's direct text input
               return user_input

       def main():
           """Main function for the text analyzer."""
           print(f"Running Python version: {sys.version_info.major}.{sys.version_info.minor}")
           
           text_to_analyze = get_text_input()

           if text_to_analyze is None:
               print("No text to analyze. Exiting.")
               return

           print("\nAnalyzing your text...")

           # Use functions from our textstats package
           words = textstats.count_words(text_to_analyze)
           chars_with_spaces = textstats.count_characters(text_to_analyze)
           chars_no_spaces = textstats.count_characters(text_to_analyze, include_spaces=False)
           lines = textstats.count_lines(text_to_analyze)

           report = textstats.format_report(words, chars_with_spaces, lines, char_count_no_spaces=chars_no_spaces)
           print(report)

       if __name__ == "__main__":
           main()

   **To Run:**
   1.  Ensure the directory structure `text_analyzer_project/textstats/` is correct with all files.
   2.  Navigate your terminal *into* the `text_analyzer_project` directory.
   3.  Run `python main_analyzer.py`.

   Python needs to be able to find the `textstats` package. When you run `main_analyzer.py` from its directory, Python automatically adds that directory to `sys.path`, so it can find the `textstats` sub-directory as a package.

----------------------------------------------------

Résumé du Module 8
==================

Félicitations pour avoir terminé le Module 8 ! Vous avez appris à structurer efficacement votre code Python en utilisant des modules et des paquets (packages), ce qui est essentiel pour construire des applications plus grandes et plus maintenables. Les points clés à retenir comprennent :

*   Les **modules** sont des fichiers `.py` qui regroupent des définitions Python apparentées.
*   L'utilisation de `import` et `from ... import` pour accéder au contenu des modules, y compris l'utilisation d'alias.
*   La **Bibliothèque Standard Python** est une riche collection de modules intégrés (`math`, `random`, `datetime`, `os`, `json`, etc.).
*   Les **paquets (packages)** sont des collections de modules organisés dans une hiérarchie de répertoires, marqués par un fichier `__init__.py`.
*   Comment créer et importer depuis vos propres paquets.
*   Le rôle de `__init__.py` dans l'initialisation des paquets et le contrôle des importations.
*   Une introduction aux **paquets tiers** de PyPI et à l'utilisation de `pip` pour l'installation et la gestion.
*   L'importance des **environnements virtuels** pour gérer les dépendances des projets.

En maîtrisant les modules et les paquets, vous pouvez écrire du code Python plus organisé, réutilisable et évolutif. Cela facilite également la collaboration avec d'autres et l'exploitation du vaste écosystème Python.

Dans le prochain module, nous introduirons un paradigme de programmation puissant : la **Programmation Orientée Objet (POO)**, qui vous permet de modéliser des entités du monde réel et leurs interactions dans votre code : :ref:`module9-oop-intro-fr` !
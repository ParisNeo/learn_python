.. _module4-data-structures-dictionaries-sets:

============================================================
Module 4: Data Structures - Dictionaries and Sets
============================================================

Welcome to Module 4! We've explored ordered collections with lists and tuples. Now, we'll dive into two more powerful Python data structures: **dictionaries** and **sets**. Dictionaries allow us to store data as key-value pairs, offering a way to look up information quickly using a custom identifier (the key). Sets, on the other hand, are unordered collections of unique items, perfect for tasks like removing duplicates or performing mathematical set operations.

.. image:: /_static/images/dict_set_mindmap.png
   :alt: Abstract representation of dictionaries (key-value) and sets (unique items)
   :width: 350px
   :align: center

Learning Objectives
-------------------

By the end of this module, you will be able to:

*   Understand and create Python dictionaries to store key-value pairs.
*   Access, add, modify, and remove items from dictionaries.
*   Iterate over dictionary keys, values, and key-value pairs.
*   Use common dictionary methods effectively.
*   Understand and create Python sets to store unique, unordered items.
*   Add and remove items from sets.
*   Perform common set operations: union, intersection, difference, and symmetric difference.
*   Understand when to use dictionaries versus sets.
*   Learn about frozensets as immutable set counterparts.

----------------------------------------------------

Dictionaries (`dict`)
=====================

A **dictionary** in Python is an unordered collection of items. While other compound data types have only values as their elements, a dictionary holds **key-value pairs**. Each key is unique within a dictionary, and it's used to access its corresponding value. Think of it like a real-world dictionary where you look up a word (the key) to find its definition (the value).

Keys must be of an immutable type (like strings, numbers, or tuples containing only immutable elements). Values can be of any data type.

Creating Dictionaries
---------------------
You can create dictionaries in several ways:

1.  **Using curly braces `{}` with key-value pairs:**
    .. code-block:: python

        # An empty dictionary
        empty_dict = {}
        print(empty_dict)       # Output: {}
        print(type(empty_dict)) # Output: <class 'dict'>

        # A dictionary of student scores
        student_scores = {"Alice": 95, "Bob": 88, "Charlie": 92}
        print(student_scores)   # Output: {'Alice': 95, 'Bob': 88, 'Charlie': 92}

        # Keys can be different immutable types (though usually consistent)
        mixed_keys_dict = {1: "one", "two": 2, (3,0): "three"}
        print(mixed_keys_dict)  # Output: {1: 'one', 'two': 2, (3, 0): 'three'}

2.  **Using the `dict()` constructor:**
    .. code-block:: python

        # From keyword arguments (keys must be valid identifiers)
        person = dict(name="Diana", age=30, city="London")
        print(person) # Output: {'name': 'Diana', 'age': 30, 'city': 'London'}

        # From a list of key-value tuples
        pairs = [("fruit", "apple"), ("color", "red")]
        fruit_info = dict(pairs)
        print(fruit_info) # Output: {'fruit': 'apple', 'color': 'red'}

Accessing Dictionary Values
---------------------------
You access dictionary values by referring to their keys inside square brackets `[]`.

.. code-block:: python

    student_scores = {"Alice": 95, "Bob": 88, "Charlie": 92}
    print(student_scores["Alice"]) # Output: 95
    # print(student_scores["David"]) # This would raise a KeyError if "David" is not a key

Using the `get()` method:
The `get(key, default_value)` method is a safer way to access values. It returns the value for `key` if `key` is in the dictionary, else `default_value`. If `default_value` is not specified, it defaults to `None`.

.. code-block:: python

    print(student_scores.get("Bob"))       # Output: 88
    print(student_scores.get("David"))     # Output: None
    print(student_scores.get("David", "Not found")) # Output: Not found

Modifying Dictionaries
----------------------
Dictionaries are mutable.

*   **Adding or Updating Items:**
    If the key exists, its value is updated. If the key doesn't exist, a new key-value pair is added.
    .. code-block:: python

        student_scores = {"Alice": 95, "Bob": 88}
        student_scores["Charlie"] = 92 # Add new item
        print(student_scores)        # Output: {'Alice': 95, 'Bob': 88, 'Charlie': 92}
        student_scores["Alice"] = 97   # Update existing item
        print(student_scores)        # Output: {'Alice': 97, 'Bob': 88, 'Charlie': 92}

*   **Removing Items:**
    *   `pop(key, default_value)`: Removes the item with the specified `key` and returns its value. Raises `KeyError` if the key is not found and no default is given.
        .. code-block:: python
            score = student_scores.pop("Bob")
            print(score)              # Output: 88
            print(student_scores)     # Output: {'Alice': 97, 'Charlie': 92}
            # missing_score = student_scores.pop("Eve") # KeyError

    *   `popitem()`: Removes and returns an arbitrary (key, value) item from the dictionary (in versions before Python 3.7, it removed a random item; in 3.7+, it removes items in LIFO order - last in, first out). Raises `KeyError` if the dictionary is empty.
        .. code-block:: python
            item = student_scores.popitem()
            print(item)               # e.g., ('Charlie', 92) if it was the last added
            print(student_scores)     # e.g., {'Alice': 97}

    *   `del dict_name[key]`: Deletes the item with the specified key. Raises `KeyError` if the key is not found.
        .. code-block:: python
            config = {"host": "localhost", "port": 8080}
            del config["port"]
            print(config) # Output: {'host': 'localhost'}

    *   `clear()`: Removes all items from the dictionary.
        .. code-block:: python
            config.clear()
            print(config) # Output: {}

Common Dictionary Methods
-------------------------
*   `keys()`: Returns a view object that displays a list of all the keys in the dictionary.
*   `values()`: Returns a view object that displays a list of all the values in the dictionary.
*   `items()`: Returns a view object that displays a list of a dictionary's key-value tuple pairs.

.. code-block:: python

    student_scores = {"Alice": 95, "Bob": 88, "Charlie": 92}
    print(student_scores.keys())   # Output: dict_keys(['Alice', 'Bob', 'Charlie'])
    print(student_scores.values()) # Output: dict_values([95, 88, 92])
    print(student_scores.items())  # Output: dict_items([('Alice', 95), ('Bob', 88), ('Charlie', 92)])

    # You can convert these view objects to lists if needed:
    key_list = list(student_scores.keys())
    print(key_list) # Output: ['Alice', 'Bob', 'Charlie']

*   `update(other_dict)`: Updates the dictionary with the key-value pairs from `other_dict`, overwriting existing keys.
    .. code-block:: python
        dict1 = {'a': 1, 'b': 2}
        dict2 = {'b': 3, 'c': 4}
        dict1.update(dict2)
        print(dict1) # Output: {'a': 1, 'b': 3, 'c': 4}

*   `copy()`: Returns a shallow copy of the dictionary.

Iterating Over Dictionaries
---------------------------
You can iterate through dictionaries in several ways:

.. code-block:: python

    student_scores = {"Alice": 95, "Bob": 88, "Charlie": 92}

    # Iterate over keys (default iteration)
    print("--- Keys ---")
    for name in student_scores:
        print(name) # Prints Alice, Bob, Charlie

    # Explicitly iterate over keys
    print("--- Keys (explicit) ---")
    for name in student_scores.keys():
        print(name)

    # Iterate over values
    print("--- Values ---")
    for score in student_scores.values():
        print(score) # Prints 95, 88, 92

    # Iterate over key-value pairs (items)
    print("--- Items ---")
    for name, score in student_scores.items():
        print(f"{name}: {score}")
    # Output:
    # Alice: 95
    # Bob: 88
    # Charlie: 92

Dictionary Comprehensions (Advanced)
------------------------------------
Similar to list comprehensions, you can create dictionaries concisely.

.. code-block:: python

    numbers = [1, 2, 3, 4]
    squared_dict = {x: x**2 for x in numbers}
    print(squared_dict) # Output: {1: 1, 2: 4, 3: 9, 4: 16}

    names = ["apple", "banana", "cherry"]
    name_lengths = {name: len(name) for name in names}
    print(name_lengths) # Output: {'apple': 5, 'banana': 6, 'cherry': 6}

When to Use Dictionaries
------------------------
*   When you need to associate unique keys with values (e.g., user IDs with user profiles).
*   For fast lookups by a unique identifier.
*   When data is naturally represented as key-value pairs (e.g., configuration settings, JSON-like data).
*   Counting frequencies of items.

----------------------------------------------------

Sets (`set`)
============

A **set** is an unordered collection of **unique** items. Sets are mutable, meaning you can add or remove items from them. They are particularly useful for membership testing, removing duplicates from a sequence, and performing mathematical set operations like union, intersection, difference, and symmetric difference.

Creating Sets
-------------
1.  **Using curly braces `{}` with comma-separated items:**
    .. code-block:: python

        # A set of integers
        numbers_set = {1, 2, 3, 4, 3, 2} # Duplicates are automatically removed
        print(numbers_set)             # Output: {1, 2, 3, 4} (order may vary)
        print(type(numbers_set))       # Output: <class 'set'>

        # A set of mixed data types (items must be hashable/immutable)
        mixed_set = {1, "hello", 3.14, (1, 2)}
        print(mixed_set)               # Output: {1, 3.14, (1, 2), 'hello'} (order may vary)

    .. important::
        To create an **empty set**, you *must* use the `set()` constructor, not `{}`.
        `empty_braces = {}` creates an empty *dictionary*.
        `empty_set = set()` creates an empty *set*.

        .. code-block:: python
            empty_s = set()
            print(empty_s)        # Output: set()
            print(type(empty_s))  # Output: <class 'set'>

2.  **Using the `set()` constructor with an iterable (e.g., list, tuple, string):**
    .. code-block:: python

        my_list = [1, 2, 2, 3, "a", "a"]
        from_list_set = set(my_list)
        print(from_list_set) # Output: {1, 2, 3, 'a'} (order may vary)

        from_string_set = set("helloo")
        print(from_string_set) # Output: {'e', 'h', 'l', 'o'} (order may vary)

Modifying Sets
--------------
*   `add(item)`: Adds an item to the set. If the item is already present, it does nothing.
    .. code-block:: python
        my_set = {1, 2}
        my_set.add(3)
        print(my_set) # Output: {1, 2, 3}
        my_set.add(2) # Adding an existing item
        print(my_set) # Output: {1, 2, 3}

*   `remove(item)`: Removes `item` from the set. Raises a `KeyError` if the item is not found.
    .. code-block:: python
        my_set = {1, 2, 3}
        my_set.remove(2)
        print(my_set) # Output: {1, 3}
        # my_set.remove(4) # Would raise KeyError

*   `discard(item)`: Removes `item` from the set if it is present. Does *not* raise an error if the item is not found.
    .. code-block:: python
        my_set = {1, 2, 3}
        my_set.discard(3)
        print(my_set) # Output: {1, 2}
        my_set.discard(4) # No error
        print(my_set) # Output: {1, 2}

*   `pop()`: Removes and returns an arbitrary item from the set. Raises `KeyError` if the set is empty.
    .. code-block:: python
        my_set = {"a", "b", "c"}
        popped_item = my_set.pop()
        print(popped_item) # e.g., 'a' (order is not guaranteed)
        print(my_set)    # e.g., {'c', 'b'}

*   `clear()`: Removes all items from the set.

Set Operations
--------------
Sets support powerful mathematical operations.

Let `A = {1, 2, 3, 4}` and `B = {3, 4, 5, 6}`

*   **Union:** Items present in either set A or set B (or both).
    *   Operator: `|`
    *   Method: `union()`
    .. code-block:: python
        A = {1, 2, 3, 4}
        B = {3, 4, 5, 6}
        union_set_op = A | B
        union_set_meth = A.union(B)
        print(union_set_op)   # Output: {1, 2, 3, 4, 5, 6}
        print(union_set_meth) # Output: {1, 2, 3, 4, 5, 6}

*   **Intersection:** Items present in both set A and set B.
    *   Operator: `&`
    *   Method: `intersection()`
    .. code-block:: python
        A = {1, 2, 3, 4}
        B = {3, 4, 5, 6}
        intersection_set_op = A & B
        intersection_set_meth = A.intersection(B)
        print(intersection_set_op)   # Output: {3, 4}
        print(intersection_set_meth) # Output: {3, 4}

*   **Difference:** Items present in set A but not in set B.
    *   Operator: `-`
    *   Method: `difference()`
    .. code-block:: python
        A = {1, 2, 3, 4}
        B = {3, 4, 5, 6}
        difference_set_op = A - B # Items in A but not B
        difference_set_meth = A.difference(B)
        print(difference_set_op)   # Output: {1, 2}
        print(difference_set_meth) # Output: {1, 2}
        print(B - A)               # Output: {5, 6} (Items in B but not A)

*   **Symmetric Difference:** Items present in either set A or set B, but not in both.
    *   Operator: `^`
    *   Method: `symmetric_difference()`
    .. code-block:: python
        A = {1, 2, 3, 4}
        B = {3, 4, 5, 6}
        sym_diff_op = A ^ B
        sym_diff_meth = A.symmetric_difference(B)
        print(sym_diff_op)   # Output: {1, 2, 5, 6}
        print(sym_diff_meth) # Output: {1, 2, 5, 6}

Other Set Methods
-----------------
*   `issubset(other_set)`: Returns `True` if all items in the set are present in `other_set`.
*   `issuperset(other_set)`: Returns `True` if all items in `other_set` are present in the set.
*   `isdisjoint(other_set)`: Returns `True` if the set has no items in common with `other_set`.

Membership Testing (`in`)
-----------------------
Checking if an item exists in a set is very efficient.

.. code-block:: python
    my_set = {"apple", "banana", "cherry"}
    print("apple" in my_set)  # Output: True
    print("grape" in my_set)  # Output: False

When to Use Sets
----------------
*   Removing duplicates from a list or other sequence.
*   Fast membership testing (checking if an item is in a collection).
*   Performing mathematical set operations (union, intersection, etc.).
*   When the order of items does not matter and you need uniqueness.

----------------------------------------------------

Frozensets (`frozenset`)
========================

A **frozenset** is an immutable version of a Python set. Once created, you cannot change its contents (add or remove items). Because they are immutable and hashable, frozensets can be used as dictionary keys or as elements of another set, which regular (mutable) sets cannot.

.. code-block:: python

    my_list = [1, 2, 3, 2, 1]
    frozen_s = frozenset(my_list)
    print(frozen_s) # Output: frozenset({1, 2, 3})

    # frozen_s.add(4) # This would raise an AttributeError

    # Can be used as a dictionary key
    my_dict = {frozen_s: "A frozen set as a key"}
    print(my_dict)  # Output: {frozenset({1, 2, 3}): 'A frozen set as a key'}

Frozensets support all non-modifying set operations and methods (like union, intersection, `issubset()`, etc.).

----------------------------------------------------

Mini-Project: Word Frequency Counter
====================================

Let's use a dictionary to count the frequency of words in a given text.

**Goal:**
1.  Take a string of text as input.
2.  Process the text:
    *   Convert it to lowercase to treat "The" and "the" as the same word.
    *   Remove common punctuation (e.g., periods, commas) or split words effectively.
3.  Count the occurrences of each word.
4.  Display the word frequencies.

**Steps:**

1.  Define a sample text string.
2.  Initialize an empty dictionary, say `word_counts`.
3.  Preprocess the text:
    *   Convert the entire text to lowercase using `text.lower()`.
    *   Consider how to handle punctuation. A simple way is to replace common punctuation marks with spaces, then split by space. More robust methods involve regular expressions (which are beyond this module's scope but good to know for future). For simplicity, we can iterate through characters and build words.
    *   Split the text into a list of words (e.g., using `text.split()`).
4.  Iterate through the list of words:
    *   For each `word`:
        *   If the `word` is already a key in `word_counts`, increment its value.
        *   If the `word` is not in `word_counts`, add it as a new key with a value of 1.
        *   (Alternatively, use `word_counts.get(word, 0) + 1`)
5.  After processing all words, iterate through the `word_counts` dictionary and print each word and its frequency.

**Example Text:**
"This is a sample text. This text is for testing the word frequency counter."

**Expected Output (order might vary):**

.. code-block:: text

    this: 2
    is: 2
    a: 1
    sample: 1
    text: 2
    for: 1
    testing: 1
    the: 1
    word: 1
    frequency: 1
    counter: 1

.. admonition:: Solution (Try it yourself before looking!)
   :class: dropdown

   .. code-block:: python

       # word_frequency_counter.py
       import string # To help with punctuation

       def count_word_frequencies(text):
           word_counts = {}
           # Convert to lowercase
           text = text.lower()

           # Remove punctuation (simple approach)
           # Create a translation table to remove punctuation
           translator = str.maketrans('', '', string.punctuation)
           text_without_punctuation = text.translate(translator)

           # Split into words
           words = text_without_punctuation.split()

           for word in words:
               if word: # Ensure word is not empty after split
                   word_counts[word] = word_counts.get(word, 0) + 1
           return word_counts

       # Example usage
       sample_text = "This is a sample text. This text is for testing the word frequency counter and this counter works!"

       frequencies = count_word_frequencies(sample_text)

       print("Word Frequencies:")
       for word, count in frequencies.items():
           print(f"{word}: {count}")

       # Example of using a set to find unique words
       # text_without_punctuation = sample_text.lower().translate(str.maketrans('', '', string.punctuation))
       # unique_words = set(text_without_punctuation.split())
       # print(f"\nUnique words: {unique_words}")
       # print(f"Number of unique words: {len(unique_words)}")

----------------------------------------------------

Module 4 Summary
================

Congratulations on completing Module 4! You've gained knowledge of two more fundamental Python data structures:

*   **Dictionaries (`dict`)** store data as **key-value pairs**, allowing for efficient data retrieval, modification, and organization when you have unique identifiers for your data.
*   **Sets (`set`)** are unordered collections of **unique items**. They are excellent for tasks like removing duplicates, fast membership checking, and performing mathematical set operations (union, intersection, etc.).
*   You also learned about **frozensets**, the immutable counterpart to sets, useful when an immutable set is required (e.g., as dictionary keys).
*   Understanding the characteristics of dictionaries (unordered, key-based access) and sets (unordered, unique items) helps you choose the right tool for various programming problems.

These structures expand your ability to model and manipulate complex data relationships in Python.

Next, we'll move on to a crucial aspect of writing larger, more organized programs: **functions**: :ref:`module5-functions`!
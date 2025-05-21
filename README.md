# Learn Python: An Open Source Course by ParisNeo

[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![View Course Online](https://img.shields.io/badge/View%20Course-Online-brightgreen)](https://parisneo.github.io/learn_python/)
[![GitHub Repository](https://img.shields.io/badge/GitHub-Repo-blue?logo=github)](https://github.com/ParisNeo/learn_python)

Welcome to "Learn Python," an open-source, beginner-friendly course designed to take you from zero to Python proficiency. This course is uniquely crafted by [ParisNeo](https://github.com/ParisNeo), leveraging AI to generate comprehensive and accessible learning materials, and is freely available for everyone.

➡️ **Access the full course online:** [https://parisneo.github.io/learn_python/](https://parisneo.github.io/learn_python/)

---

## 🌟 About This Course

This course aims to provide a solid foundation in Python programming. Whether you're completely new to coding or looking to pick up Python as a new skill, these modules are structured to guide you step-by-step. The content is generated with the assistance of AI, then curated and refined by ParisNeo to ensure quality and clarity.

## 🎯 What You'll Learn

*   **Python Fundamentals:** Understand what Python is and why it's popular.
*   **Core Concepts:** Variables, data types, operators, and user input.
*   **Control Flow:** Making decisions with `if/elif/else` and repeating actions with `for` and `while` loops.
*   **Data Structures:** Working with Lists, Tuples, Dictionaries, and Sets.
*   **Functions:** Writing reusable blocks of code, understanding scope, and lambda functions.
*   **Hands-on Practice:** Mini-projects in each module to solidify your understanding.
*   *(More modules covering advanced topics like Error Handling, File I/O, OOP, etc., are planned!)*

## 📖 Course Structure

The course is divided into modules, each focusing on specific aspects of Python:

*   **Module 0:** Getting Started - The Launchpad (`module0-getting-started-fr.rst`)
*   **Module 1:** Variables, Data Types, and User Input (`module1-variables-and-data-types-fr.rst`)
*   **Module 2:** Control Flow - Making Decisions and Repeating Actions (`module2-control-flow-fr.rst`)
*   **Module 3:** Data Structures - Lists and Tuples (`module3-data-structures-lists-tuples-fr.rst`)
*   **Module 4:** Data Structures - Dictionaries and Sets (`module4-data-structures-dictionaries-sets-fr.rst`)
*   **Module 5:** Functions - Writing Reusable Code (`module5-functions-fr.rst`)
    *   *(Currently the course content is in French, indicated by "_fr" in filenames. English versions may be added in the future.)*

## 🛠️ How It's Built

*   **Content Generation:** AI-assisted content creation, curated by ParisNeo.
*   **Format:** Written in reStructuredText (`.rst`).
*   **Documentation Tool:** Built using [Sphinx](https://www.sphinx-doc.org/).
*   **Hosting:** Served via [GitHub Pages](https://pages.github.com/).

## 🚀 Getting Started (Locally)

If you want to build or contribute to the course locally:

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/ParisNeo/learn_python.git
    cd learn_python
    ```
2.  **Set up a Python environment** (virtual environment recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```
3.  **Install dependencies** (Sphinx and any theme/extensions used, e.g., `sphinx-rtd-theme`):
    ```bash
    pip install sphinx sphinx-rtd-theme
    # Add any other dependencies listed in a requirements.txt if available
    ```
4.  **Build the HTML documentation:**
    (Assuming your `conf.py` and `.rst` files are in the root or a `docs/` subdirectory. Adjust the command if your source directory is different.)
    ```bash
    # If conf.py is in the root:
    sphinx-build -b html . _build/html
    # Or if you have a Makefile (common with sphinx-quickstart):
    # make html
    ```
5.  **View the documentation:**
    Open `_build/html/index.html` in your web browser.

## 🤝 Contributing

Contributions are highly welcome! Whether it's fixing a typo, improving an explanation, adding a new mini-project, translating content, or suggesting a new module, your input is valuable.

1.  **Fork** the repository.
2.  Create a new **branch** for your feature or fix (`git checkout -b feature/your-amazing-feature`).
3.  Make your changes.
4.  **Commit** your changes (`git commit -am 'Add some amazing feature'`).
5.  **Push** to the branch (`git push origin feature/your-amazing-feature`).
6.  Open a **Pull Request**.

Please ensure your contributions adhere to the existing style and structure.

## 📜 License

This project is licensed under the **Apache 2.0 License**. See the [LICENSE](LICENSE) file for details.

```
(You will need to create a `LICENSE` file in your repository root and paste the full text of the Apache 2.0 License into it. You can find the text here: https://www.apache.org/licenses/LICENSE-2.0.txt)
```

## 🧑‍💻 Author

*   **ParisNeo** - [GitHub Profile](https://github.com/ParisNeo)

---

Happy Learning!

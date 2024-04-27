**Lesson 1: Setting up Python and Basic Syntax**

**Installing Python**

Before we dive into the world of Python, you'll need to have Python installed on your computer. Here are the steps to install Python:

**Windows:**

1. Go to the official Python download page and click on the "Download Python" button.
2. Select the latest version of Python (currently Python 3.x) and click on the "Download Now" button.
3. Run the installer and follow the prompts to install Python.

**Mac (via Homebrew):**

1. Open Terminal on your Mac.
2. Install Homebrew by running the following command: `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`
3. Install Python using Homebrew by running the following command: `brew install python`

**Linux (Ubuntu-based distributions):**

1. Open Terminal on your Linux machine.
2. Install Python using the package manager by running the following command: `sudo apt-get install python3`

**Basic Syntax**

Now that you have Python installed, let's take a look at the basic syntax of the language.

**Indentation**

In Python, indentation is used to denote block-level structure. This means that you'll use spaces or tabs to indent your code to show which lines belong to a particular block. For example:

```
if True:
    print("Hello, world!")
```

In this example, the `print` statement is indented under the `if` statement, indicating that it belongs to the `if` block.

**Variables and Assignment**

In Python, you can assign a value to a variable using the assignment operator (=). For example:

```
x = 5
y = "hello"
```

Here, we've assigned the value `5` to the variable `x` and the string `"hello"` to the variable `y`.

**Basic Data Types**

Python has several basic data types:

- **Integers**: Whole numbers, e.g. `1`, `2`, `3`, etc.
- **Floats**: Decimal numbers, e.g. `3.14`, `-0.5`, etc.
- **Strings**: Sequences of characters, e.g. `"hello"`, `'hello'`, etc. Strings can be enclosed in single quotes or double quotes.
- **Booleans**: True or false values, e.g. `True`, `False`

**Basic Operators**

Python has several basic operators:

- **Arithmetic Operators**:
  - `+` (addition)
  - `-` (subtraction)
  - `*` (multiplication)
  - `/` (division)
  - `**` (exponentiation)
- **Comparison Operators**:
  - `==` (equal to)
  - `!=` (not equal to)
  - `>` (greater than)
  - `<` (less than)
  - `>=` (greater than or equal to)
  - `<=` (less than or equal to)
- **Logical Operators**:
  - `and` (logical and)
  - `or` (logical or)
  - `not` (logical not)

**Basic Syntax Examples**

Here are some examples of basic syntax in Python:

```
# Assign a value to a variable
x = 5

# Print a string
print("Hello, world!")

# Use arithmetic operators
result = 2 + 3
print(result)  # Output: 5

# Use comparison operators
x = 5
y = 3
print(x > y)  # Output: True

# Use logical operators
x = 5
y = 3
print(x > y and x < 10)  # Output: True
```

That's it for Lesson 1! You've learned how to install Python, basic syntax, and basic data types. In the next lesson, we'll dive deeper into control structures.

**Exercises**

1. Install Python on your computer if you haven't already.
2. Write a Python program that prints "Hello, world!" to the screen.
3. Assign the value `10` to a variable `x` and print its value.
4. Use the `+` operator to add `2` and `3` and store the result in a variable `result`. Print the value of `result`.

**Next Lesson**

In the next lesson, we'll cover control structures such as if-else statements and loops.

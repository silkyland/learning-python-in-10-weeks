Here is Lesson 3: Functions.

**Lesson 3: Functions**

Welcome to Lesson 3 of our Python 101 series! In this lesson, we'll cover functions in Python.

**What are Functions?**

In Python, a function is a block of code that can be executed multiple times from different parts of your program. Functions allow you to organize your code into reusable blocks, making your program more modular and easier to maintain.

**Defining a Function**

To define a function in Python, you use the `def` keyword followed by the function name and parentheses. For example:

```
def greet(name):
    print("Hello, " + name + "!")
```

In this example, we've defined a function called `greet` that takes a single argument `name`.

**Calling a Function**

To call a function, you simply type the function name followed by parentheses containing the arguments. For example:

```
greet("John")
```

This would print "Hello, John!" to the console.

**Function Arguments**

Functions can take multiple arguments, which are separated by commas. For example:

```
def add(x, y):
    return x + y
```

In this example, the `add` function takes two arguments `x` and `y` and returns their sum.

**Return Values**

Functions can also return values, which can be assigned to variables or used in expressions. For example:

```
result = add(2, 3)
print(result)  # prints 5
```

**Lambda Functions**

Lambda functions are small, anonymous functions that can be defined inline. They are often used as arguments to higher-order functions. For example:

```
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers)  # prints [1, 4, 9, 16, 25]
```

In this example, we've defined a lambda function that takes a single argument `x` and returns its square. We then use the `map` function to apply this lambda function to each element of the `numbers` list.

**Example Code**

Here's an example code snippet that demonstrates the use of functions:

```
def greet(name):
    print("Hello, " + name + "!")

greet("John")

def add(x, y):
    return x + y

result = add(2, 3)
print(result)  # prints 5

numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers)  # prints [1, 4, 9, 16, 25]
```

This code snippet demonstrates the use of functions, function arguments, return values, and lambda functions.

**Exercises**

1. Write a Python program that defines a function to calculate the area of a rectangle.
2. Write a Python program that defines a function to calculate the factorial of a number.
3. Write a Python program that defines a function to convert Celsius to Fahrenheit.
4. Write a Python program that defines a function to filter out even numbers from a list.

**Next Lesson**

In the next lesson, we'll cover working with data in Python, including lists, tuples, dictionaries, and sets.

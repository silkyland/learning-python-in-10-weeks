**Lesson 7: Advanced Topics**

Welcome to Lesson 7 of our Python 101 series! In this lesson, we'll cover advanced topics in Python, including list comprehensions, generators, and decorators.

**List Comprehensions**

A list comprehension is a concise way to create a new list from an existing list or other iterable. It consists of an expression followed by a `for ` clause and zero or more `if ` clauses. For example:

```
numbers = [1, 2, 3, 4, 5]
squared_numbers = [x**2 for x in numbers]
print(squared_numbers)  # [1, 4, 9, 16, 25]
```

This code creates a new list `squared_numbers` that contains the squares of the numbers in the original list `numbers`.

**Generators**

A generator is a special type of function that returns an iterator, which allows you to iterate over a sequence of values without storing them all in memory at once. For example:

```


def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1


gen = infinite_sequence()
for _ in range(10):
    print(next(gen))  # prints 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
```

This code defines a generator function `infinite_sequence` that yields an infinite sequence of numbers. The `next` function is used to retrieve the next value from the generator.

**Decorators**

A decorator is a special type of function that takes another function as an argument and returns a new function that "wraps" the original function. Decorators are often used to add additional functionality to existing functions. For example:

```


def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper


@my_decorator
def say_hello():
    print("Hello!")


say_hello()
```

This code defines a decorator `my_decorator` that takes a function as an argument and returns a new function that wraps the original function. The `@ my_decorator` syntax is used to apply the decorator to the `say_hello` function.

**Example Code**

Here's an example code snippet that demonstrates the use of list comprehensions, generators, and decorators:

```
numbers = [1, 2, 3, 4, 5]
squared_numbers = [x**2 for x in numbers]
print(squared_numbers)  # [1, 4, 9, 16, 25]


def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1


gen = infinite_sequence()
for _ in range(10):
    print(next(gen))  # prints 0, 1, 2, 3, 4, 5, 6, 7, 8, 9


def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper


@my_decorator
def say_hello():
    print("Hello!")


say_hello()
```

This code snippet demonstrates the use of list comprehensions, generators, and decorators.

**Exercises**

1. Write a Python program that uses a list comprehension to create a new list of squares of numbers from 1 to 10.
2. Write a Python program that uses a generator to iterate over a sequence of numbers from 1 to 10.
3. Write a Python program that uses a decorator to add additional functionality to a function.

**Congratulations!**

You've reached the end of our Python 101 series! I hope you've learned a lot about Python and are ready to start building your own projects. Remember to practice regularly and experiment with different concepts to reinforce your learning. Good luck with your Python journey!

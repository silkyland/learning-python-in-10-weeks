Here is Lesson 4: Working with Data.

**Lesson 4: Working with Data**

Welcome to Lesson 4 of our Python 101 series! In this lesson, we'll cover working with data in Python, including lists, tuples, dictionaries, and sets.

**Lists**

A list is a collection of items that can be of any data type, including strings, integers, floats, and other lists. Lists are defined using square brackets `[]` and elements are separated by commas. For example:

```
fruits = ["apple", "banana", "cherry"]
```

You can access elements of a list using their index, which starts at 0. For example:

```
print(fruits[0])  # prints "apple"
```

You can also modify elements of a list using their index. For example:

```
fruits[0] = "orange"
print(fruits)  # prints ["orange", "banana", "cherry"]
```

**Tuples**

A tuple is similar to a list, but it is immutable, meaning its elements cannot be modified after it is created. Tuples are defined using parentheses `()` and elements are separated by commas. For example:

```
numbers = (1, 2, 3, 4, 5)
```

You can access elements of a tuple using their index, just like with lists. For example:

```
print(numbers[0])  # prints 1
```

**Dictionaries**

A dictionary is a collection of key-value pairs, where each key is unique and maps to a specific value. Dictionaries are defined using curly braces `{}` and key-value pairs are separated by commas. For example:

```
person = {"name": "John", "age": 30, "city": "New York"}
```

You can access values in a dictionary using their keys. For example:

```
print(person["name"])  # prints "John"
```

You can also modify values in a dictionary using their keys. For example:

```
person["age"] = 31
print(person)  # prints {"name": "John", "age": 31, "city": "New York"}
```

**Sets**

A set is an unordered collection of unique elements. Sets are defined using the `set()` function or curly braces `{}`. For example:

```
numbers = {1, 2, 3, 4, 5}
```

You can add elements to a set using the `add()` method. For example:

```
numbers.add(6)
print(numbers)  # prints {1, 2, 3, 4, 5, 6}
```

You can also remove elements from a set using the `remove()` method. For example:

```
numbers.remove(4)
print(numbers)  # prints {1, 2, 3, 5, 6}
```

**Example Code**

Here's an example code snippet that demonstrates the use of lists, tuples, dictionaries, and sets:

```
fruits = ["apple", "banana", "cherry"]
print(fruits[0])  # prints "apple"

numbers = (1, 2, 3, 4, 5)
print(numbers[0])  # prints 1

person = {"name": "John", "age": 30, "city": "New York"}
print(person["name"])  # prints "John"

numbers = {1, 2, 3, 4, 5}
numbers.add(6)
print(numbers)  # prints {1, 2, 3, 4, 5, 6}
```

This code snippet demonstrates the use of lists, tuples, dictionaries, and sets.

**Exercises**

1. Write a Python program that defines a list of numbers and calculates their sum.
2. Write a Python program that defines a tuple of strings and prints each element.
3. Write a Python program that defines a dictionary of person data and prints each value.
4. Write a Python program that defines a set of numbers and adds a new element.

**Next Lesson**

In the next lesson, we'll cover object-oriented programming in Python, including classes and objects.

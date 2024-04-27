**Lesson 5: Object-Oriented Programming**

Welcome to Lesson 5 of our Python 101 series! In this lesson, we'll cover object-oriented programming (OOP) in Python, including classes and objects.

**Classes and Objects**

In OOP, a class is a blueprint for creating objects. A class defines the properties and behavior of an object. An object is an instance of a class, and it has its own set of attributes (data) and methods (functions).

**Defining a Class**

To define a class in Python, you use the `class` keyword followed by the name of the class. For example:

```
class Dog:
    pass
```

This defines a class called `Dog`.

**Attributes**

Attributes are the data that an object has. In Python, you can define attributes inside the `__init__` method of a class. The `__init__` method is a special method that is called when an object is created. For example:

```
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

This defines a class `Dog` with two attributes: `name` and `age`.

**Methods**

Methods are functions that belong to a class. In Python, you can define methods inside a class using the `def` keyword. For example:

```
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print("Woof!")
```

This defines a class `Dog` with a method `bark` that prints "Woof!".

**Creating Objects**

To create an object, you use the class name followed by parentheses. For example:

```
my_dog = Dog("Fido", 3)
```

This creates an object `my_dog` of type `Dog` with attributes `name` = "Fido" and `age` = 3.

**Accessing Attributes and Methods**

You can access an object's attributes and methods using the dot notation. For example:

```
print(my_dog.name)  # prints "Fido"
my_dog.bark()  # prints "Woof!"
```

**Inheritance**

Inheritance is a mechanism in OOP that allows one class to inherit the attributes and methods of another class. In Python, you can use the `class` keyword followed by the name of the parent class in parentheses. For example:

```
class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def bark(self):
        print("Woof!")
```

This defines a class `Dog` that inherits from `Animal`.

**Example Code**

Here's an example code snippet that demonstrates the use of classes and objects:

```
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print("Woof!")

my_dog = Dog("Fido", 3)
print(my_dog.name)  # prints "Fido"
my_dog.bark()  # prints "Woof!"
```

This code snippet demonstrates the use of classes and objects.

**Exercises**

1. Write a Python program that defines a class `Rectangle` with attributes `width` and `height`, and a method `area` that calculates the area of the rectangle.
2. Write a Python program that defines a class `Person` with attributes `name` and `age`, and a method `greet` that prints a greeting message.
3. Write a Python program that defines a class `Vehicle` with attributes `make` and `model`, and a method `start_engine` that prints a message indicating that the engine has started.
4. Write a Python program that defines a class `BankAccount` with attributes `balance` and `account_number`, and a method `deposit` that adds a deposit to the balance.

**Next Lesson**

In the next lesson, we'll cover file input/output and exception handling in Python.

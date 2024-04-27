**Lesson 2: Control Structures**

**Conditional Statements**

In Python, conditional statements are used to execute different blocks of code based on certain conditions. The most common type of conditional statement is the `if` statement.

**If Statement**

The `if` statement is used to execute a block of code if a certain condition is true. The syntax for an `if` statement is:

```
if condition:
    # code to execute if condition is true
```

For example:

```
x = 5
if x > 10:
    print("x is greater than 10")
```

In this example, the code inside the `if` block will not be executed because the condition `x > 10` is false.

**If-Else Statement**

The `if-else` statement is used to execute a block of code if a certain condition is true, and another block of code if the condition is false. The syntax for an `if-else` statement is:

```
if condition:
    # code to execute if condition is true
else:
    # code to execute if condition is false
```

For example:

```
x = 5
if x > 10:
    print("x is greater than 10")
else:
    print("x is less than or equal to 10")
```

In this example, the code inside the `else` block will be executed because the condition `x > 10` is false.

**Elif Statement**

The `elif` statement is used to check another condition if the initial condition is false. The syntax for an `elif` statement is:

```
if condition:
    # code to execute if condition is true
elif another_condition:
    # code to execute if another_condition is true
```

For example:

```
x = 5
if x > 10:
    print("x is greater than 10")
elif x == 5:
    print("x is equal to 5")
```

In this example, the code inside the `elif` block will be executed because the condition `x > 10` is false, but the condition `x == 5` is true.

**Loops**

Loops are used to execute a block of code repeatedly for a specified number of times. Python has two types of loops: `for` loops and `while` loops.

**For Loop**

The `for` loop is used to execute a block of code for each item in a sequence (such as a list or string). The syntax for a `for` loop is:

```
for variable in sequence:
    # code to execute for each item in sequence
```

For example:

```
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```

In this example, the code inside the `for` loop will be executed three times, once for each item in the `fruits` list.

**While Loop**

The `while` loop is used to execute a block of code as long as a certain condition is true. The syntax for a `while` loop is:

```
while condition:
    # code to execute while condition is true
```

For example:

```
x = 0
while x < 5:
    print(x)
    x += 1
```

In this example, the code inside the `while` loop will be executed five times, until the condition `x < 5` is false.

**Break and Continue Statements**

The `break` statement is used to exit a loop prematurely. The `continue` statement is used to skip the current iteration of a loop and move on to the next iteration.

For example:

```
for x in range(5):
    if x == 3:
        break
    print(x)
```

In this example, the loop will exit when `x` is equal to 3.

```
for x in range(5):
    if x == 3:
        continue
    print(x)
```

In this example, the iteration when `x` is equal to 3 will be skipped.

**Exercises**

1. Write a Python program that uses an `if` statement to print "Hello, world!" if a variable `x` is greater than 10.
2. Write a Python program that uses an `if-else` statement to print "x is greater than 10" if a variable `x` is greater than 10, and "x is less than or equal to 10" otherwise.
3. Write a Python program that uses a `for` loop to print each item in a list of fruits.
4. Write a Python program that uses a `while` loop to print the numbers from 0 to 4.

**Next Lesson**

In the next lesson, we'll cover functions in Python.

print("hello world")
print("Sawasdee krub")
print("Hello", "world", sep=", ")  # print with separator

# more print examples with format or good example for noob
print("I have {0} apples".format(5))
print("I have {} apples".format(5))  # same as above
print("{0} + {1} = {2}".format(1, 2, 1+2))
print("{a} + {b} = {sum}".format(a=1, b=2, sum=1+2))  # named placeholder
print("{0:0>4}".format(1))  # left pad with 0, at least 4 characters
print("{0:0<4}".format(1))  # right pad with 0, at least 4 characters
print("{0:.2f}".format(1.2345))  # print with 2 decimal places

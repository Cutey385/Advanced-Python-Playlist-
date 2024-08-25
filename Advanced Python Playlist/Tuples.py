# Tuple: ordered, immutable, allows duplicate elements

my_tuple = ("Max", 28, "Boston")
print(f"my_tuple: {my_tuple}")

# Without the parentheses, it is still a tuple.

my_tuple = "Max", 28, "Boston"
print(f"my_tuple: {my_tuple}")

# If there is only one element, it doesn't get recognized as a tuple. If you put a comma after it, it gets recognized.

my_tuple = ("Max")
print("Type of my_tuple:", type(my_tuple))

my_tuple = ("Max",)
print("Type of my_tuple:", type(my_tuple))

# To define a tuple, you can use 'tuple()' function.

my_tuple = tuple(["Max", 28, "Boston"])
print(f"my_tuple: {my_tuple}")

# Accessing elements

item = my_tuple[2]
print("my_tuple[2] =", item)

item = my_tuple[-2]
print("my_tuple[-2] =", item)

# Iterating

print("The elements in my_tuple: ")

for i in my_tuple:
    print(i)

# Checking for an element

if "Max" in my_tuple:
    print("Max is in the tuple")
else:
    print("Max is not in the tuple")

# Other useful methods

my_tuple = ('a', 'p', 'p', 'l', 'e')
print("The length of the tuple is " + str(len(my_tuple)))
print("The number of 'p's in the tuple is " + str(my_tuple.count('p')))
print("The index of the first 'p' in the tuple is", my_tuple.index('p'))

# Tuples can be converted into lists and lists can be converted into tuples.

my_list = list(my_tuple)
print("my_list:", my_list)
print(my_list)

my_tuple = tuple(my_list)
print("my_tuple:", my_tuple)

# Slicing

a = (1, 2, 3, 4, 5, 6, 7, 8, 9)

b = a[2:5]
print("b:", b)

# If you don't specify a start index, it starts all the way from the beginning.

b = a[:6]
print("b:", b)

# If you don't specify a stop index, it goes all the way to the end.

b = a[1:]
print("b:", b)

# Stepping

b = a[::2]
print("b:", b)

b = a[::-1]
print("b:", b)
# Unpacking

my_tuple = ("Max", 28, "Boston")
name, age, city = my_tuple
print("name: ", name)
print("age:", age)
print("city:", city)

my_tuple = (0, 1, 2, 3, 4)
i1, *i2, i3 = my_tuple
print("i1:", i1)
print("i3:", i3)
print("*i2:", *i2)    # If you don't use '*', it will give you the list format.

# Tuples are more memory efficient than lists.

import sys
import timeit

my_list = [23, "good", False, 456]
my_tuple = (23, "good", False, 456)
print("Size of my_list:", sys.getsizeof(my_list), "bytes")
print("Size of my_tuple:", sys.getsizeof(my_tuple), "bytes")

# It takes much more time to create a list than to create a tuple.

print("Time taken to create a list:", timeit.timeit(stmt="[1, 2, 3, 4, 5]", number=1000000))
print("Time taken to create a tuple:", timeit.timeit(stmt="(1, 2, 3, 4, 5)", number=1000000))

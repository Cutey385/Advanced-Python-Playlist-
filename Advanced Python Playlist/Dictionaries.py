# Dictionary: Key-Value pairs, Unordered, Mutable

mydict = {"name": "Max", "age": 28, "city": "New York"}
print(mydict)

# You can use the 'dict()' function to define a dictionary.

mydict2 = dict(name="Mary", age=27, city="Boston")
print(mydict2)

# Accessing to the values

value = mydict["name"]
print(value)

# Overriding

mydict["email"] = "max@xyz.com"
print(mydict)

mydict["email"] = "coolmax@xyz.com"
print(mydict)

# Deleting items

del mydict["city"]
print(mydict)

mydict.pop("age")
print(mydict)

# popitem() deletes the last element in the dictionary.

mydict.popitem()
print(mydict)

# Checking if a key is in the dictionary

if "name" in mydict:
    print(mydict["name"])
else:
    print("There is no such key.")

try:
    print(mydict["lastname"])
except:
    print("Error")

# Looping through a dictionary

for key in mydict.keys():    # "for key in mydict:" gives the keys as well
    print(key)

for value in mydict.values():
    print(value)

for key, value in mydict.items():
    print(key, value)

# Copying a dictionary

mydict_copy = mydict

# If you modify the copy of the dictionary, the original gets modified too, in this way of copying.

mydict_copy["email"] = "max@xyz.com"
print(mydict_copy)
print(mydict)

#  If you do not want that, use this:

mydict_copy2 = mydict.copy()

mydict_copy2["age"] = 28
print(mydict_copy2)
print(mydict)

# The "dict()" function creates a shallow copy of the dictionary, which does not modify the original dictionary directly

mydict_copy3 = dict(mydict)

mydict_copy3["city"] = "Boston"
print(mydict_copy3)
print(mydict)

# Merging dictionaries

my_dict = {"name": "Max", "age": 28, "email": "max@xyz.com"}
my_dict_2 = dict(name="Mary", age=27, city="Boston")

my_dict.update(my_dict_2)
print(my_dict)

# Numbers and tuples can be used as dictionary keys, but lists cannot because they are mutable.

my_dict = {3: 9, 6: 36, 9: 81}
print(my_dict)

value = my_dict[9]
print(value)

my_tuple = (8, 7)
mydict = {my_tuple: 15}
print(mydict)

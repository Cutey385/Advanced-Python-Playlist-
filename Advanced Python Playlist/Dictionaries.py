# Dictionary: Key-Value pairs, Unordered, Mutable

mydict = {"name": "Max", "age": 28, "city": "New York"}
print(mydict)

# You can use the 'dict()' function to define a dictionary

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

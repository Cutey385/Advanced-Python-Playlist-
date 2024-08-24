# Sets: unordered, mutable, no duplicates

myset = {1, 2, 3}
print(f"myset: {myset}")

myset = {1, 2, 3, 1, 2}    # Sets do not allow duplicates.
print(f"myset: {myset}")

myset = set([1, 2, 3])
print(f"myset: {myset}")

myset = set("Hello")     # Since sets are unordered collections, the order of the elements in the output may vary.
print(f"myset: {myset}")

# Empty curly braces are recognized as a dictionary type.

myset = {}
print(f"Type of myset: {type(myset)}")

# So, if you want to define an empty set, use the set() function.

myset = set()
print(f"Type of myset: {type(myset)}")

myset.add(1)
myset.add(2)
myset.add(3)

myset.remove(3)     # If you try to 'remove' a non-existing element, it will raise an error.
myset.discard(5)    # Whereas discard does nothing if the element is not a member.
print(f"myset: {myset}")

myset.clear()    # Clears the set.
print(f"myset: {myset}")

myset = {1, 23, 6, 7}

print(f"Removed element: {myset.pop()}")    # 'pop()' method removes and returns an arbitrary element from the set
print(f"myset: {myset}")

# Iteration

print("Elements in the set:")
for i in myset:
    print(i)

# Checking for an element

if 1 in myset:
    print("Does 1 exist in the set? Yes")
else:
    print("Does 1 exist in the set? No")

# Union and intersection

odds = {1, 3, 5, 7, 9}
evens = {0, 2, 4, 6, 8}
primes = {2, 3, 5, 7}

u = odds.union(evens)
print(f"Union of odds and evens: {u}")

i = odds.intersection(evens)
print(f"Intersection of odds and evens: {i}")

i2 = odds.intersection(primes)
print(f"Intersection of odds and primes: {i2}")

# Difference

setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}

diff = setA.difference(setB)    # Gives the elements in setA that are not in setB
print(f"Difference: {diff}")

diff = setB.difference(setA)    # Gives the elements in setB that are not in setA
print(f"Difference: {diff}")

diff = setA.symmetric_difference(setB)
print(f"Difference: {diff}")    # Gives elements in either setA or setB, but not in both

setA.update(setB)    # Adds all elements of setB to setA (only elements not already in setA are added)
print(f"setA: {setA}")

setA.intersection_update(setB)    # Updates setA to keep only the elements that are also in setB
print(f"setA: {setA}")

setA.difference_update(setB)    # Removes all elements from setA that are also in setB
print(f"setA: {setA}")

setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}

print(f"setA: {setA}")

setA.symmetric_difference_update(setB)     # Updates setA to contain only elements unique to setA or setB
print(f"setA: {setA}")

# Subset, superset and disjoint

print(f"Is setA a subset of setB: {setA.issubset(setB)}")     # Checks if all elements of setA are in setB

print("Is setB a superset of {1, 2, 3, 10, 11, 12}:", setB.issuperset({1, 2, 3, 10, 11, 12}))

print("Are setA and setB disjoint:", setA.isdisjoint(setB))    # Checks if setA and setB have no elements in common

# Copying two sets

setA = {1, 2, 3, 4, 5, 6}

setB = setA    # Assigns setA to setB (both variables refer to the same set object)
setB.add(7)    # Adds the element 7 to setB (and setA, since they refer to the same set)
print(f"setB: {setB}")
print(f"setA: {setA}")

setB = setA.copy()    # Creates a copy of setA and assigns it to setB (setB is now a separate set with the same elements as setA)
setB.add(8)
print(f"setB: {setB}")
print(f"setA: {setA}")    # setA remains unchanged from its original state

setB = set(setA)    # Creates a new setB from setA
setB.add(9)
print(f"setB: {setB}")
print(f"setA: {setA}")    # setA remains unchanged

# frozenset

a = frozenset([1, 2, 3, 4])    # Creates an immutable set a (frozenset) that does not support add or remove operations

# Frozensets support set operations like union, intersection, and difference.

print("a:", a)











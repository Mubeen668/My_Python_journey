'''
Collections are used to store multiple no.of values to a single VARIABLE.
In python those types are : List, Tuple, Set, Dictionary.
'''

# SET
# sets are unordered collection of elements which are mutable(changeable).
# main thing in the sets are they do not allow duplicates and denoted by curly braces {}
# it can have any data types (int, strings, float and boolean).

# Example to create a set
S1 = {1, 2, "Hi", 4.78, True, "hello", 7, 9.9, False, ("a", "b", "c")}
print(S1)

# we can also create an empty set
S2 = set()

# we cannot access elements in a set using because they are unordered
# so we can access them using for loop

# Example to iterate through a set
for item in S1:
    print(item, end=" ")  # Output: 1 2 Hi 4.78 True hello 7 9.9 False ('a', 'b', 'c')

# Example to check if an element exists in the set
if "hello" in S1:
    print("\n'hello' exists in S1")  # Output: 'hello' exists in S1

# Example to add an element to the set using add() method
S1.add(26)
print(S1) # this will add 26 at end of the set

# Example to remove an element from the set using remove() method
S1.remove(26)   
print(S1)      # this will remove 26 from the set


# Example to clear all elements from the set using clear() method
# S1.clear()
# print(S1)  # Output: set() (empty set)

# Example to find the length of the set using len() method
print(len(S1))  # Output: length of the set

# Example to convert a set to a list using list() method
set_to_list = list(S1)
print(set_to_list)  # this converts S1 into the list

# Example to convert a set to a tuple using tuple() method
set_to_tuple = tuple(S1)
print(set_to_tuple)  # this converts S1 into the tuple

# Example to check if two sets are equal using == operator
s3 = { 1,5,4}
s4 = { 2,5,4}
print(s3 == s4) # Output: False (because they are not equal)

# important set methods

# Example to find the union of two sets using union() method
s5 = s3.union(s4)
print(s5)  # Output: {1, 2, 4, 5}

# Example to find the intersection of two sets using intersection() method
s6 = s3.intersection(s4)
print(s6)  # Output: {4, 5} (common elements)

# Example to find the difference of two sets using difference() method
s7 = s3.difference(s4)
print(s7)  # Output: {1} (elements in s3 but not in s4)

# Example to find the symmetric difference of two sets using symmetric_difference() method
s8 = s3.symmetric_difference(s4)
print(s8)  # Output: {1, 2} (elements in either s3 or s4 but not in both)

# Example to check if a set is a subset of another set using issubset() method
s9 = {1, 4}
print(s9.issubset(s3))  # Output: True (because 1 and 4 are in s3)

# Example to check if a set is a superset of another set using issuperset() method
print(s3.issuperset(s9))  # Output: True (because s3 contains all elements of s9)



# Example to find the maximum and minimum elements in a set using max() and min() methods
s3 = { 1,5,4}
max_element = max(s3)
min_element = min(s3)
print(f"Max : {max_element}, Min : {min_element}")  # Output: Max : 5, Min : 1

# Example to find the sum of all elements in a set using sum() method
print(sum(s3)) 

# Example to find the product of all elements in a set using a loop
product = 1
for num in s3:
    product *= num
print(f"Product: {product}")  # Output: Product: 20 

# Example to find the average of all elements in a set
average = sum(s3) / len(s3)
print(f"Average: {average}")  
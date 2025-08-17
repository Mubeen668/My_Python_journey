'''
Collections are used to store multiple no.of values to a single VARIABLE.
In python those types are : List, Tuple, Set, Dictionary.
'''
# TUPLE
# tuple is a ordered  collection of elements which are immutable(unchageable).
# Allow duplicates and denoted in parenthesis ()
# it can have any data types (int, strings, float and boolean).

# Example to create a tuple
tuple1 = (1, 2, "Hi", 4.78, True, "hello", 7, 9.9, False, ("a", "b", "c"))  
print(tuple1)

# we can also create an empty tuple
tuple2 =()

# we can access elements in a tuple using indexing and it starts from 0 and also have the negative indexing
print(tuple1[0])  # Output: 1
print(tuple1[2])  # Output: Hi  
print(tuple1[5])  # Output: hello
print(tuple1[9])  # Output: ('a', 'b', 'c')

# We can also access elements from the end of the tuple using negative indexing starts from -1
print(tuple1[-1])  # Output: ('a', 'b', 'c')    
print(tuple1[-2])  # Output: False
print(tuple1[-3])  # Output: 9.9  etc...

# since tuples are immutable we cannot change values or update values in a tuple
#  tuple1[0] =10 # this will gives an error

# methods in tuple
# 1. Example to count the occurrences of an element in the tuple using count() method
count = tuple1.count(1)
print(f"Count of 1 in tuple1: {count}")  # Output: Count of 1 in tuple1: 1

# 2. Example to find the index of an element in the tuple using index() method
index = tuple1.index("Hi")
print(f"Index of 'Hi' in tuple1: {index}")  # Output: Index of 'Hi' in tuple1: 2

# 3. Example to convert a tuple to a list using list() method
# tuple_to_list = list(tuple1)
# print(tuple_to_list) # this converts tuple1 into the list



# 4. Example to check if an element exists in the tuple
if "hello" in tuple1:
    print("'hello' exists in tuple1")  # Output: 'hello' exists in tuple1

# 5. Example to iterate through a tuple
for item in tuple1: 
    print(item, end=" ")  # Output: 1 2 Hi 4.78 True hello 7 9.9 False ('a', 'b', 'c')

# 6. Example to unpack a tuple into variables
t2 = ("hello", 6)
a, b = t2
print(f"\nUnpacked values: {a}, {b}") # Output: Unpacked values: hello, 6

# 7. Example to concatenate two tuples
tuple3 = tuple1 + t2
print(tuple3) # Output: (1, 2, 'Hi', 4.78, True, 'hello', 7, 9.9, False, ('a', 'b', 'c'), 'hello', 6)

# 8. Example to repeat a tuple
tuple4 = t2 * 3
print(tuple4)  # Output: ('hello', 6, 'hello', 6, 'hello', 6)

# Example to find the length of a tuple
print(len(tuple1))





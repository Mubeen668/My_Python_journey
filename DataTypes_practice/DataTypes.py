# int data type
print(type(42))    # <class 'int'>
print(isinstance(42, int))  # True

# Float data type
print(type(3.14))   # <class 'float'>
print(isinstance(3.14, float))  # True

# String data type
str = "Hello, World!"
print(type(str))   # <class 'str'>
print(isinstance(str, str))  # True

# bool data type
print(bool("Hello")) # True
print(bool(15)) # True
print(bool("")) # False


# Simple program to check '==' and 'is' both are same or not
a = [1,2,3]
b = [1,2,3]
print(a == b)  # True
print(a is b)  # False 
# reason: '==' checks for value equality, while 'is' checks for identity (same object in memory)
# 'a' and 'b' have the same values but are different objects in memory.


'''
Collections are used to store multiple no.of values to a single VARIABLE.
In python those types are : List, Tuple, Set, Dictionary.
'''
# List
# A list is a collection which is ordered and changeable. Allows duplicate values.
# Lists can have any data types (int,string,float,boolean, and list itself).

# Example to create a list
List = [1,2,"Hi",4.78,True,"hello",7,9.9,False,["a","b","c"]]

# we can also creata empty list
EmptyList = []

# Example to access elements in a list using index and it starts from 0
print(List[0])  # Output: 1
print(List[2])  # Output: Hi
print(List[5])  # Output: hello
print(List[9])  # Output: ['a', 'b', 'c']
print(List[8])  # Output: False

# We can also access elements from the end of the list using negative indexing starts from -1
print(List[-1])  # Output: ['a', 'b', 'c']
print(List[-2])  # Output: False
print(List[-3])  # Output: 9.9  etc...

# Example to change the value of an element in a list
List[0] = 10
print(List)  # it will replace the first element with 10 from 1

# list METHODS

# 1. Example to add an element to the end of the list we use append() method
List.append("New Element")
print(List)  # it will add "New Element" to the end of the list

# 2. Example to insert an element at a specific index using insert(position, values to be insert) method
List.insert(2, "Inserted Element")
print(List)  # it will insert "Inserted Element" at index 2

# 3. Example to remove an element from the list using remove() method
List.remove("hello")
print(List)  # it will remove the first occurrence of "hello" from the list

# 4. Example to remove the last element from the list using pop() method
List.pop()
print(List)  # it will remove the last element from the list

# 5. Example methos to sort the list using sort() method
List1 = [3, 1, 4, 2, 5]
List1.sort()
print(List)  # it will sort the list in ascending order

# 6. Example to extend the list with another list using extend() method
List2 = [6, 7, 8]
List1.extend(List2)
print(List1)  # it will add elements of List2 to the end of List1

# 7. Example to count the occurrences of an element in the list using count() method
c = List.count(1)
print(c)  # it will count how many times 1 is present in the list

# 8. one more thing is 'del' keyword can be used to remove an element from the list
del List[0]  # it will delete the first element from the list
print(List)  

# 9. there a clear() method which will remove all elements from the list and make it empty
List1.clear()  
print(List1)  # it will print an empty list []

# 10. length of the list can be found using len() function
print(len(List))  # it will print the number of elements in the list



# in LISTs we have important thing that is LIST COMPREHENSION
# List comprehension is a concise way to take inpute/create lists in Python.

# syntax is: '[expression for item in iterable if condition]'

# Example of list comprehension to create a new list with squares of numbers from 0 to 9
squares = [x**2 for x in range(10)]
print(squares)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Example of list comprehension with a condition to create a new list with even numbers from 0 to 9
even_numbers = [x for x in range(10) if x % 2 == 0]
print(even_numbers)  # Output: [0, 2, 4, 6, 8]

# Example of list comprehension to create a new list with strings converted to uppercase
words = ["hello", "world", "python"]
uppercase_words = [word.upper() for word in words]
print(uppercase_words)  # Output: ['HELLO', 'WORLD', 'PYTHON']

# simple program1
l1 = [1, 2, 3, 4, 5]
l2 = [x**2 if x % 2 == 0 else x for x in l1]
print(l2)  # it will print squares to the even numbers and keep same for odd numbers


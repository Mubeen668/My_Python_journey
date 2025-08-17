'''
Collections are used to store multiple no.of values to a single VARIABLE.
In python those types are : List, Tuple, Set, Dictionary.
'''

# Dictionary
# A dictionary is an unordered collection of key-value pairs, they are mutable(changeable).
# Each key is unique and is used to access its corresponding value.

# Example to create a dictionary
D1 = {
    "name": "pandu",
    "age": 25,
    "city": "Vij"
}
print(D1)

# Example to create an empty dictionary
D2 = {}

# Example to access a value using its key
print(D1["name"])  # Output: pandu

# Example to add a new key-value pair to the dictionary
D1["fav_hero"] = "mahesh babu"
print(D1) # Output: {'name': 'pandu', 'age': 25, 'city': 'Vij', 'fav_hero': 'mahesh babu'}

# Example to remove a key-value pair using the del keyword
del D1["age"]
print(D1)  

# Example to clear all key-value pairs from the dictionary using clear() method
# D1.clear()
# print(D1)  # Output: {}

# Example to find the length of the dictionary using len() method
print(len(D1))  # Output: length of the dictionary

# Example to check if a key exists in the dictionary using the 'in' keyword
if "city" in D1:
    print("'city' exists in D1")  # Output: 'city' exists in D1

# Example to iterate through the keys of the dictionary
for key in D1:
    print(key, end="\n")  # Output: name fav_hero city
print()

# Example to iterate through the values of the dictionary
for value in D1.values():
    print( value, end="\n")  # Output: pandu mahesh babu Vij
print()

# Example to iterate through the key-value pairs of the dictionary
for key, value in D1.items():
    print(f"{key}: {value}", end="\n")  # Output: name: pandu fav_hero: mahesh babu city: Vij



# Example to convert a dictionary to a list of keys using list() method
dict_to_keys_list = list(D1.keys())
print(dict_to_keys_list)  # Output: ['name', 'fav_hero', 'city']


# Example to convert a dictionary to a list of values using list() method
dict_to_values_list = list(D1.values())
print(dict_to_values_list)  # Output: ['pandu', 'mahesh babu', 'Vij']


# Example to check if two dictionaries are equal using == operator
D3 = {
    "name": "GeMu",
    "age": 25,
    "city": "Vij"
}
print(D1 == D3)  # Output: False (because they are not equal)


# Example to merge two dictionaries using the update() method   
D1.update(D3)
print(D1)  # Output: {'name': 'GeMu', 'fav_hero': 'mahesh babu', 'city': 'Vij', 'age': 25}


# Example to get the value of a key using get() method
value = D1.get("name")
print(value)  

# Example to get the value of a key that does not exist using get() method with a default value
value = D1.get("country")
print(value)  


# Example to copy a dictionary using the copy() method
D4 = D1.copy()
print(D4)  

# Example to check if a dictionary is empty using the bool() function
is_empty = bool(D2)
print(is_empty)  # Output: True (because D2 is empty)





# learning more about strings and their methods in python

str = "Hello, World!"
print(str) # o/p: Hello, World!

# string retrieve
print(str[0])  # o/p: H
print(str[7])  # o/p: W , 
# these are positive index based retrieval ( positive index starts from 0 to n-1), 
# 'n'is the lenghth of the string which is number of charcters in the string including spaces and punctuation.


# we can also retrieve using negative index
print(str[-1])  # o/p: ! (last character)
print(str[-2])  # o/p: d (second last character) etc..

# string slicing
print(str[0:5])  # o/p: Hello (from index 0 to 4)
print(str[7:12])  # o/p: World (from index 7 to 11# string reverse with slicing

# String slicing with step
print(str[::2])  # o/p: Hlo ol! (prints every second character)
print(str[1::2])  # o/p: e,Wrd (prints every second character starting from index 1)

# String join
words = ["Hello", "World"]
print(" ".join(words))  # o/p: Hello World (joins the list of words with a space)


# string length
print(len(str))  # o/p: 13 (length of the string)

# string concatenation
str2 = " How are you?"
print(str + str2)  # o/p: Hello, World! How are you?

# string repetition
print(str * 2)  # o/p: Hello, World!Hello, World!, because it multiplies the string by 2

# Reseversing the string with slicing
string = input() # input taken from the user
print(str[::-1]) # o/p: the string in reverse order 

# string methods
str = "Hello, World!"
print(str.lower())  # O/p: hello, world! (converts to lowercase)
print(str.upper())  # o/p: HELLO, WORLD! (converts to uppercase)
print(str.strip())  # o/p: Hello, World! (removes leading and trailing whitespace)
print(str.replace("World", "Python"))  # o/p: Hello, Python! (replaces substring)
print(str.split(","))  # o/p: ['Hello', ' World!'] (splits the string into a list)   
print(str.find("World"))  # o/p: 7 (finds the index of the substring "World", which is a starting index of word "World")
print(str.count("o"))  # o/p: 2 (counts occurrences of 'o')

# string formatting
name = "Alice"
age = 30
formatted_str = f"My name is {name} and I am {age} years old."

print(formatted_str)  # o/p: My name is Alice and I am 30 years old.

# Escape characters
str = "We are the so-called \"Vikings\" from the north."    
print(str)  # o/p: We are the so-called "Vikings" from the north.   

if ' ' in str:
    print("yes")  # o/p: yes (checks if space is present in the string)
else:
    print("no")


# String comparison
str1 = "apple"
str2 = "banana"
print(str1 < str2)  # o/p: True (compares lexicographically
print(str1 > str2)  # o/p: False
print(str1 == str2)  # o/p: False (checks for equality)

# String iteration
for char in str:
    print(char, end=' ')  # o/p: H e l l o ,   W o r l d ! (prints each character in the string)

# String membership
print('H' in str)  # o/p: True (checks if 'H' is in the string)
print('x' in str)  # o/p: False (checks if 'x' is in the string)



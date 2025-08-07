''' 
Loops : loops are used to execute a block of repeatedly until that specific conditions is true 
        or for a specific no.of iterations
        Loops are 2 types 1. For loop and 2. While loop
'''
''' 
Now we will see for loop : for loop is used to run a block of code for a certain range or used to iterate thorw collections
'''
# syntax of for loop : " for variable in iterable/ range(start, end, step):"


# Example of for loop with range
for i in range(1, 11):  # here range is from 1 to 10 (1 to 11 is not included)
    print(i)            # it will print numbers from 1 to 10  


# Example of for loop with a list
fruits = ["apple", "banana", "cherry"]
for i in fruits:  # here fruit is the variable which will take each value from the list fruits
   print(i)       # it will print each fruit in the list

# Example of for loop with a string
message = "hello, world"

for char in message:
    print(char, end="")      # it will print each character in the string message in horizontal line


# simple program to print even numbers from 1 to 5 using for loop

for i in range(1, 6):
    if i % 2 ==0:
        print(f"even number: {i}")  # it will print even numbers from 1 to 5
    else:
        print(f"odd number:{i}")    # it will print even numbers from 1 to 5


# multiplication table using for loop

num = int(input("enter a number to print multiplication table:"))

for i in range(1, 11):
    print(f'{num} X {i} = {num * i}') # it will print multiplication table of the given number from 1 to 10


# simple program to find factorial of a number using for loop

n = int(input("enter a number to find factorial: "))
fact =1
for i in range(1,n+1):
    fact *= i
print(f"factorail of the given number {n} is {fact}")


# simple program to find factors
n = int(input("enter a number to find factors: "))
print(f"factors of {n} are: ", end="")
for i in range(1, n + 1):
    if n % i == 0:
        print(i, end=" ")  # it will print all the factors of the given number

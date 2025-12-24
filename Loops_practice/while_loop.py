''' 
Loops : loops are used to execute a block of code repeatedly until that specific conditions is true 
        or for a specific no.of iterations
        Loops are 2 types 1. For loop and 2. While loop
'''
''' 
Now we will see while loop : while loop is used to run a block of code until the condition is true
'''
# syntax of while loop : " while condition:"

# Example of while loop
count = 1  
while count <= 10:  # here condition is count less than or equal to 10
    print(count)     # it will print numbers from 1 to 10
    count += 1      # incrementing count by 1 in each iteration


# simple program to print even numbers from 1 to 5 using while loop
count = 1
while count <= 5:      
    if count % 2 == 0:
        print(f"even number: {count}")  # it will print even numbers from 1 to 5
    else:
        print(f"odd number: {count}")    # it will print odd numbers from 1 to 5
    count += 1


# multiplication table using while loop
num = int(input("enter a number to print multiplication table: "))  
count = 1
while count <= 10:  
    print(f'{num} X {count} = {num * count}')  # it will print multiplication table of the given number from 1 to 10
    count += 1

# simple program to find factorial of a number using while loop
n = int(input("enter a number to find factorial: "))    
fact = 1
count = 1
while count <= n:  
    fact *= count  
    count += 1     # here we need to incrementing count by 1 in each iteration
print(f"factorial of the given number {n} is {fact}")  


# simple program to find factors using while loop
n = int(input("enter a number to find factors: "))
count = 1
while count <=n:
    if n % count == 0:
        print(count, end=" ")  # it will print all the factors of the given number
    count += 1  


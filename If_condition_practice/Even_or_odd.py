# with if condition we can check a number is even or odd
num = int(input("Enter a number: "))
if num % 2 == 0:
    print(f"{num} is even")
else:
    print(f"{num} is odd")


# with if condition we can check a number is positive, negative or zero
num = int(input("Enter a number: "))
if num > 0:
    print(f"{num} is positive")
elif num < 0:
    print(f"{num} is negative")
else:
    print("The number is zero")
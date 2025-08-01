# with if condition we can check a string is palindrome or not
str_input = input("Enter a string: ")
if str_input == str_input[::-1]:
    print(f"{str_input} is a palindrome")
else:
    print(f"{str_input} is not a palindrome")



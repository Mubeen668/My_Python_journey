# Here we will know about the '__name__' variable and the 'if __name == "__main__" ' condition.
# lets understand this with WHAT, WHY, HOW and WHEN.

# WHAT is __name__ variable?
# __name__ is a built-in variable in Python that represents the name of the current module.
# When a Python file is run directly, the __name__ variable is set to "__main__".
# However, when the file is imported as a module in another script, the __name__ variable is set to the name of the module.


# WHY do we use 'if __name__ == "__main__"' condition?
# The 'if __name__ == "__main__"' condition is used to check whether a Python file is being run directly or being imported as a module.
# When the file is run directly, the code inside the 'if __name__ == "__main__"' block will be executed.
# soo , when the file is imported as a module, the code inside the block will not be executed.

# HOW to use 'if __name__ == "__main__"' condition?
# To use the 'if __name__ == "__main__"' condition, you need to define a function (usually named main()) that contains the code you want to execute when the file is run directly.
# Then, you can use the 'if __name__ == "__main__"' condition to call the main() function.
# For example:
def add(a,d,b=-2,c=-4):
    return a+b+c+d  
def main():
    print("This main function is running...***")
    print(add(4,7))
if __name__ == "__main__":
    main()      


# WHEN to use 'if __name__ == "__main__"' condition?
# You should use the 'if __name__ == "__main__"' condition when you want to create a Python file that can be run both as a standalone script and as a module in another script.
# This is especially useful when you want to test your code or provide a command-line interface for your module.
# By using the 'if __name__ == "__main__"' condition, you can ensure that the code inside the block is only executed when the file is run directly, and not when it is imported as a module.
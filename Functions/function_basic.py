# Function :-  functions are the block of reusable codes , we group related code together and use it when needed.
# when our program has a lot of code, we can group related code together as small chunks of code called functions.

# To declare a function we a keyword " def " and then the function name.
# syntax:  'def fun_name():'

# simple example program 
def Sample_func():
    print("Sample function ")
# calling the function
Sample_func()

# to print the result from the function we need to call that function 
# Present we have seen a simple function without arguments and return values.
# ARGUMENTS : arguments are the values that we pass to a function as parameters in the function definition.

# There are 4 types of Arguments we have ;- 
# 1. Default Arguments, 2. Keyword Arguments, 3. Arbitrary Arguments, 4. Positional Arguments.

# 1. Default Arguments:
# Default arguments are the values that are passed to a function if NO value is provided to the variable.

# Example of Default Arguments:
def Subtract(a,b=6):
    return a-b

result = Subtract(22)     
# Here we're passing only one value, that is for 'a' and for 'b' we are assign a default value  6 in the function definition. 
# so every time we call this function without passing the second argument, it will use the default value of 'b' which is 6.
print(result)


# 2. Keyword Arguments:
# Keyword arguments are the arguments that are passed to a function by explicitly specifying the parameter name and its value.
# This allows us to pass arguments in any order, as long as we specify the parameter names.

def Multiply(a, b=2):
    return a * b
result = Multiply(b=7,a=6)  # Here we are passing the arguments in different order and 'b' varible will take the value 7. 
# so remember in the keyword arguments the passing order doesn't matter,
# as long as we specify the parameter names.
print(result)


# 3. Arbitrary Arguments:
# Arbitrary arguments allow us to pass a more number of arguments to a function.
# This is achieved by the symbol '*', it is also called as unpacking operator.

def Add(*args):
    total=0
    for i in args:
        total += i
    return total
result = Add(34,56,76,12,33,45,554,3,23)  # here we're passing multiple arguments to the function
print(result)

# 4. Positional Arguments:
# Positional arguments are the arguments that are passed to a function in the order they are defined.
def add(a, b):
    return a + b
result = add(100, 5)  # Here we are passing the arguments in the order they are defined.
print(result)


# Few points we need to remember about functions:
# 1. Functions can return a value using the 'return' statement.
# 2. If a function does not have a return statement, it will return 'None' by default.
# 3. in Arguments we can pass any data type like string, list, tuple, dictionary, etc.
# ***4. order of parameters in the function definition matters most, 
#      ----> PASS THE PARAMETERS WITHOUT DEFAULT VALUES FIRST THEN FOLLOWS PARAMETERS WITH DEFAULT VALUES.


# In function Arbitrary arguments we have 2 more things *args and **kwargs.
# 1. '*args' is used to pass a variable number of non-keyword arguments to a function. 
#       It allows us to pass any number of positional arguments to the function.

# eample of *args:
def sample_args(*a,b):    # Here 'a' will take all the positional arguments passed to the function and 'b' will take the keyword argument.
    t=0
    print(type(a))  # it will print class of 'a' which is a tuple.
    for values in a:
        t += (values + b)
    return t

result = sample_args(1, 2, 3, 4, b=10)  # Here we are passing multiple positional arguments and one keyword argument 'b'.
print(result)

# ***** important note about *args:  here *args takes values as a TUPLE, and with the help of '*' we can unpack the TUPLE.


# 2. '**kwargs' is used to pass a variable number of keyword arguments to a function.
#       It allows us to pass any number of keyword arguments to the function.

# example of **kwargs:
def sample_kwargs(**kwargs):
    print(type(kwargs))  # it will print class of 'kwargs', which is a dictionary(dict).
    for key,value in kwargs.items():
        print(f"{key} = {value}")
result = sample_kwargs(name="GeeMu", age=23, city="Nandigama")  # Here we are passing multiple keyword arguments to the function.

# ***** important note about **kwargs:  here **kwargs takes values as a DICTIONARY, and with the help of '*' we can unpack the TUPLE.


# Decorators -- Decorators are the functions, which modifies the behaviour of the another function
#               it takes another function as an argument and add aditional functionalities to the function.
# example use cases are Logging, Timers, Caching etc...

# Example program

def my_decorator(func):
    def wrapper():
        print("Before -- in the additional functionality")
        func()
        print("After -- in the additional functionality")
    return wrapper

@my_decorator
def say_hello():
    print("Main function ")

say_hello()


# Example program with arguments

def my_decorator(func):
    def wrapper(name):
        print("Additional functionality before the main function runs")
        func(name)
        print("Additional functionality after the main function runs")
    return wrapper
@my_decorator
def greet(name):
    print(f"hello {name}")

greet("pandu")
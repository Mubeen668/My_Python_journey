# Inheritance -- Inheritance is allows a class to inherit from another class
#                which means that it takes attributes and methods from the parent classes
#                with this we get reusability of the code
#                Child <- Parent  or   Sub class <- Super class


# let's take an Example of a car 

class car:             # Parent class or Super class
    def __init__(self,name,color):
        self.name = name
        self.color = color

    def move(self):
        print(f"{self.name} is moving.....")
    
class mini_car(car):    # Child class or Sub class
    def describe(self):
        print(f"This car is a mini version of {self.name} and it's color is {self.color}....")


CAR1 = mini_car("TATA_svu","Burgendy")
CAR1.move()
CAR1.describe()


# hope u understand some basics of inheritance
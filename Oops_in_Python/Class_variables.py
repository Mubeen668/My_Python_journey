# In Oops we have class variables 
# Class variables -- are defined outside of the Constructor
#                    it shared among all the instances of class

# example program

class car:
    model_year = 2024  # This is a class variable

    def __init__(self, name, color):
        self.name = name   # These are instance variables
        self.color = color

car1 = car("Renolt","red")
# we can access class variables using instances :
# print(f"car details \n name: {car1.name} \n color: {car1.color} \n model year: {car1.model_year}")


# we can access class variable using class name also :
print(f"car details \n name: {car1.name} \n color: {car1.color} \n model year: {car.model_year}")
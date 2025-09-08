# Now we learn most important topic that is Object Oriented Programming (OOPs)
#( Note : naku emi radu emaina tappulu vunte please excuseme and correct them if you know well)


# first of all OOPs is programming paradigm in python it uses the "objects" and "classes"
# OBJECT -- is an instance of a class / Any real world entity
#           And it is a bundle which groups the related ATTRIBUTES and METHODS 

# Ex -- condiser a pen is an object 
#        Attributes -- color, type, brand, price
#        Methods -- write(), refill(), cap(), uncap()

# CLASS -- is a blueprint or template for objects

# let's see a simple example to understand this

class car:
    def __init__(self, name, model):
        self.name = name      # These are ATTRIBUTES and also called INSTANCE VARIABLES 
        self.model =  model   
    
    def describe(self):    # This is a METHOD to the class
        print(f"these are the details of a car :- \n name: {self.name} and \n model: {self.model}")
        
car1 = car("BMW", 2020)
car1.describe()


# Here one more thing we need to talk i.e. CONSTRUCTOR
# CONSTRUCTOR -- is a special method which is automatically called when an object of a class is created
#                It is used to initialize the attributes of the class
#                In python the constructor is defined using __init__() method
# SELF -- is a special keyword which is used to access the attributes and methods of the class
#         It is the first parameter of the constructor and methods of the class


# I hope u will understand some basics about oops along with me......
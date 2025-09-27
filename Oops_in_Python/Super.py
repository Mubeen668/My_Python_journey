# Super() -- super function in python is allows us to call methods from a parent class within child class.
#            It is commonly used in inheritance to access parent class methods and attributes. 

print("---- Super() function in Python----\n")
class parent:
    def show(self):
        print("This is parent class")
class child(parent):
    def show(self):
        super().show()  # calling parent class method using super()
        print("This is child class")
obj = child()
obj.show()  

print("*************************************")

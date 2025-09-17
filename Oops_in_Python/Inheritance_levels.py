# Multiple inheritance  -- This allows a class to inherit attributes & methods from multiple parent classes (more than one parent class)

# consider an example for this is Phone
print("---- Multiple Inheritance----\n")
class mobile:   
    def __init__(self,model_year,brand):
        self.model_year = model_year
        self.brand = brand
    def specs(self):
       print(f"This mobile made in {self.model_year} and it was launched by {self.brand} brand")

class Brand:
    def maker(self):
        print("This mobile is made by Oneplus")

class Buy(mobile, Brand):
    pass

'''
Mobile = mobile(2022,"Oneplus")
Brand = brand()
'''
item = Buy(2022,"Oneplus")
item.specs()
item.maker()

print("*************************************")

print("---- Multilevel Inheritance----\n")
# Multilevel inheritance -- here a class is inherit from a parent which is also inherited from another parent class

class teacher:
    def subject(self):
        print("Teacher explaining DSA..")

class my_topper_frnd(teacher):
    def teach(self):
        print("My topper frnd learns from teacher")

class me(my_topper_frnd):
    def learns(self):
        print("Initially I didn't understand what teachers says so i learn from my frnd...")

obj = me()
obj.subject()
obj.teach()
obj.learns()
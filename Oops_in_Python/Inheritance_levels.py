# Multiple inheritance  -- This allows a class to inherit attributes and methods from multiple parent classes (more than one parent class)

# consider an example for this is Phone

class mobile:   
    def __init__(self,model_year,brand):
        self.model_year = model_year
        self.brand = brand

class brand:
    def maker(self):
        print(f"This mobile is made by {self.brand}")

class Buy(mobile, brand):
    def purchase(self):
       print(f"This mobile made in {self.model_year} and its {self.brand} brand")

'''
Mobile = mobile(2022,"Oneplus")
Brand = brand()
'''
item = Buy(2022,"Oneplus")
item.purchase()
item.maker()




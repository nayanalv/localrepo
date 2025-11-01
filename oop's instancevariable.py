#What are Instance Variables?
'''Instance variables are variables that are bound to a specific instance (object) of a class. 
Each object of a class has its own copy of instance variables, meaning they store data unique to
each instance'''

class Car:
    def __init__(self, make, model):
        self.make = make       # instance variable
        self.model = model     # instance variable

# Creating instances (objects) of the class
car1 = Car("Toyota", "Corolla")
car2 = Car("Honda", "Civic")

# Accessing instance variables
print(car1.make)  # Outputs: Toyota
print(car2.make)  # Outputs: Honda


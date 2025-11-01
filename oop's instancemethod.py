#What are Instance Methods?
'''Instance methods are functions that belong to a specific instance of a class. 
They operate on the instance's data (instance variables) and define the behavior of an object.
Instance methods always take at least one parameter, which is typically named self. 
self refers to the specific instance of the class on which the method is being called.'''

class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    
    # Instance method
    def start_engine(self):
        print(f"The {self.make} {self.model}'s engine has started.")

# Creating an instance
car1 = Car("Toyota", "Corolla")

# Calling an instance method
car1.start_engine()  # Outputs: The Toyota Corolla's engine has started.
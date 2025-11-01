#why we need class? what is class ? How class will work?
#A class is like a blueprint for creating objects. An object is an instance of a class. 
#Each object has attributes (also called properties) and methods (functions associated with the object).
#Attributes store data about the object (e.g., color, brand, speed).
#Methods are functions that define the behavior of the object (e.g., accelerate, brake).
# Define the Car class
class Car:
    # Initializer (Constructor) - This method is called when a new Car object is created
    def __init__(self, make, model, year, color, is_electric=False):
        # Attributes of the car (the data we associate with the car)
        self.make = make  # String type
        self.model = model  # String type
        self.year = year  # Integer type
        self.color = color  # String type
        self.is_electric = is_electric  # Boolean type (default is False)
        self.speed = 0  # Integer type to track the car's speed
        self.past_speeds = []  # List type to track the history of speeds

    # Method to accelerate the car
    def accelerate(self, increment):
        self.speed += increment  # Increase the speed
        self.past_speeds.append(self.speed)  # Store the new speed in past_speeds list
        print(f"The {self.make} {self.model} is now going {self.speed} km/h.")

    # Method to brake the car
    def brake(self, decrement):
        self.speed -= decrement  # Decrease the speed
        if self.speed < 0:
            self.speed = 0  # Speed can't be negative
        self.past_speeds.append(self.speed)
        print(f"The {self.make} {self.model} slowed down to {self.speed} km/h.")

    # Method to display car details
    def display_details(self):
        electric_status = "Electric" if self.is_electric else "Non-Electric"
        print(f"Car Details: {self.year} {self.make} {self.model}, {self.color}, {electric_status}")
        print(f"Past Speeds: {self.past_speeds}")

# Creating objects (instances) of the Car class, car1 and car2 are the object/instances of the class car
car1 = Car(make="Tesla", model="Model 3", year=2023, color="Red", is_electric=True)
car2 = Car(make="Ford", model="Mustang", year=2020, color="Blue", is_electric=False)

# Using methods on the objects
car1.display_details()
car1.accelerate(30)
car1.accelerate(50)
car1.brake(20)
car1.display_details()

car2.display_details()
car2.accelerate(40)
car2.brake(30)
car2.display_details()

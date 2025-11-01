#what is object?why we need object ?How it will work?
'''An object is a fundamental concept in object-oriented programming (OOP). 
It can be thought of as a real-world entity or a thing that has both:
Attributes (properties): These are characteristics or data that describe the object.
Methods (functions): These are actions or behaviors that the object can perform.'''

# Why Do We Need Objects?

'''Objects are the building blocks of object-oriented programming, and they help in organizing and 
structuring code in a more modular and understandable way.

The main reasons we use objects are:

Encapsulation:
Objects help in bundling related data (attributes) and behaviors (methods) into a single unit. This reduces complexity because you only need to interact with the object as a whole, rather than managing each attribute and method separately.
For example, a Car object might have attributes like color, model, engineType, and methods like start(), stop(), and accelerate().

Abstraction:
Objects provide a way to hide the complex details and only expose the necessary functionality. This allows you to work with the object at a higher level without worrying about how it works internally.
For example, you don’t need to know how a start() method works to start a car; you just call the method.

Reusability:
Once an object is created (or a class, which is a blueprint for creating objects), you can reuse it in other parts of your program without having to rewrite the same code. You can even create new objects based on existing ones.

Inheritance:
Objects can inherit properties and methods from other objects, which allows for code reuse and extending functionality without modifying the original object. This helps in reducing code duplication.

Modularity:
Objects make it easier to break down complex programs into smaller, manageable, and reusable pieces (modules). Each object can handle a specific task and interact with other objects to achieve a larger goal.'''

# How Objects Work?
'''Classes and Instantiation:
A class is like a blueprint or template for creating objects. It defines the structure (attributes) and behavior (methods) that the objects created from the class will have.
When you want to create an object, you instantiate the class. This means you create an instance of that class (an object).'''

# Example in Python
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start(self):
        print(f"{self.year} {self.make} {self.model} is starting.")

# Create an object (instance of the Car class)
my_car = Car("Toyota", "Corolla", 2020)

# Accessing attributes and calling methods
print(my_car.make)  # Output: Toyota
my_car.start()      # Output: 2020 Toyota Corolla is starting.
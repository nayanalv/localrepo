#why we need constructor? what is constructor in class ? How constructor will work?
#The constructor in Python (denoted by __init__) is essential for creating and initializing objects of a class.
# It provides a way to set up the initial state of an object when it is created
#The constructor (__init__) is automatically called when you create an instance of a class. 
# Its main job is to initialize the attributes(name,age,city) of the object (i.e., give it an initial state).
# Without a constructor, you'd have to manually initialize every object after creating it, which is inefficient and error-prone.

class Person:
    def __init__(self, name, age, city):
        # Constructor initializes the object attributes
        self.name = name
        self.age = age
        self.city = city

# Creating an instance of the Person class
person1 = Person("Alice", 30, "New York")

# Now person1 has its attributes initialized right away
print(person1.name)  # Alice
print(person1.age)   # 30
print(person1.city)  # New York

#Without the __init__ constructor:
# You’d have to create an instance and then manually assign attributes afterward:

# person1 = Person()
# person1.name = "Alice"
# person1.age = 30
# person1.city = "New York"
# This manual initialization is more prone to errors and takes longer to do, especially when dealing with many attributes.


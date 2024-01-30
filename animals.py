# Sample Python Code for IntelliSense Testing

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        """Produce a sound."""
        pass

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, species="Dog")
        self.breed = breed

    def make_sound(self):
        """Bark like a dog."""
        return "Woof!"

# Creating an instance of the Dog class
my_dog = Dog(name="Buddy", breed="Labrador")

# Accessing attributes with IntelliSense
print(my_dog.name)     # As you type "my_dog.", IntelliSense suggests "name" and "breed"
print(my_dog.breed)    # IntelliSense suggests "breed"

# Calling methods with IntelliSense
my_dog.make_sound()    # As you type "my_dog.make_sound()", IntelliSense suggests "make_sound"

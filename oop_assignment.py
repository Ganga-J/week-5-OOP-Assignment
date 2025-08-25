#
# Assignment 1: Design Your Own Class!

class Smartphone:
    """A class representing a generic smartphone."""
    # The constructor to initialize an object's attributes
    def __init__(self, brand, model, os, storage_gb):
        self.brand = brand
        self.model = model
        self.os = os
        self.storage_gb = storage_gb
        self.is_on = False 

    # A method to turn the phone on
    def turn_on(self):
        """Turns the smartphone on."""
        if not self.is_on:
            self.is_on = True
            print(f"The {self.brand} {self.model} is now on.")
        else:
            print(f"The {self.model} is already on.")

    # A method to display information about the phone
    def display_info(self):
        """Prints the details of the smartphone."""
        print("-" * 20)
        print("Smartphone Details:")
        print(f"  Brand: {self.brand}")
        print(f"  Model: {self.model}")
        print(f"  OS: {self.os}")
        print(f"  Storage: {self.storage_gb} GB")
        print("-" * 20)


class FoldableSmartphone(Smartphone):

    """A subclass representing a foldable smartphone."""
    def __init__(self, brand, model, os, storage_gb, is_folded=True):
        super().__init__(brand, model, os, storage_gb)
        self.is_folded = is_folded

    def fold(self):
        """Folds the phone."""
        if not self.is_folded:
            self.is_folded = True
            print(f"The {self.model} is now folded.")
        else:
            print(f"The {self.model} is already folded.")
            
    def display_info(self):
        """Overrides the parent method to include folded status."""
        super().display_info()
        print(f"  Folded Status: {'Folded' if self.is_folded else 'Unfolded'}")

# Creating instances (objects) of our classes
my_phone = Smartphone("Google", "Pixel 8 Pro", "Android", 256)
my_foldable_phone = FoldableSmartphone("Samsung", "Galaxy Z Fold5", "Android", 512, is_folded=False)

# Using the methods on our objects
my_phone.display_info()
my_phone.turn_on()
print("\n" + "=" * 30 + "\n")
my_foldable_phone.display_info()
my_foldable_phone.fold()
print("\n" + "=" * 30 + "\n")

#
# Activity 2: Polymorphism Challenge! 

class Vehicle:
    """A generic class for a vehicle."""
    def move(self):
        """Defines the move action for a generic vehicle."""
        print("A generic vehicle is moving.")

# A subclass of Vehicle
class Car(Vehicle):
    """A car moves by driving."""
    def move(self):
        """Overrides the parent method to show the car's specific action."""
        print("Driving... 🚗")

# Another subclass of Vehicle
class Plane(Vehicle):
    """A plane moves by flying."""
    def move(self):
        """Overrides the parent method to show the plane's specific action."""
        print("Flying... ✈️")

# A list containing objects of different classes
vehicles = [Vehicle(), Car(), Plane()]

# Demonstrating polymorphism
print("Polymorphism Demonstration:")
for v in vehicles:
    v.move()


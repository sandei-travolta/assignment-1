# Assignment 1: Design Your Own Class!
class Smartphone:
    def __init__(self, brand, model, battery):
        self.brand = brand
        self.model = model
        self.battery = battery  # in percentage

    def call(self, number):
        print(f"{self.brand} {self.model} is calling {number}...")

    def charge(self, amount):
        self.battery = min(100, self.battery + amount)
        print(f"{self.brand} {self.model} charged to {self.battery}%.")

# Inheritance layer
class GamingSmartphone(Smartphone):
    def __init__(self, brand, model, battery, cooling_system):
        super().__init__(brand, model, battery)
        self.cooling_system = cooling_system

    def play_game(self, game):
        print(f"{self.brand} {self.model} is playing {game} with {self.cooling_system} cooling.")

# Activity 2: Polymorphism Challenge!
class Vehicle:
    def move(self):
        print("Vehicle is moving.")

class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

class Boat(Vehicle):
    def move(self):
        print("Sailing 🚤")

# Example usage:
if __name__ == "__main__":
    # Smartphone example
    phone = Smartphone("Apple", "iPhone 14", 50)
    phone.call("123-456-7890")
    phone.charge(30)

    gaming_phone = GamingSmartphone("Asus", "ROG Phone", 80, "liquid")
    gaming_phone.play_game("PUBG Mobile")
    gaming_phone.charge(10)

    # Polymorphism example
    vehicles = [Car(), Plane(), Boat()]
    for v in vehicles:
        v.move()
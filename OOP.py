#Assignment 1: Smartphone Class Design

# Base Class: Smartphone
class Smartphone:
    def __init__(self, brand, model, storage, battery):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.battery = battery
        self.is_on = False
    
    def power_on(self):
        if not self.is_on:
            self.is_on = True
            print(f"{self.brand} {self.model} is now ON.")
        else:
            print(f"{self.brand} {self.model} is already ON.")
    
    def power_off(self):
        if self.is_on:
            self.is_on = False
            print(f"{self.brand} {self.model} is now OFF.")
        else:
            print(f"{self.brand} {self.model} is already OFF.")
    
    def charge(self, amount):
        if self.battery + amount <= 100:
            self.battery += amount
            print(f"{self.brand} {self.model} charged to {self.battery}%.")
        else:
            self.battery = 100
            print(f"{self.brand} {self.model} is fully charged.")

# Derived Class: SmartphoneWithCamera (inherits from Smartphone)
class SmartphoneWithCamera(Smartphone):
    def __init__(self, brand, model, storage, battery, camera_megapixels):
        super().__init__(brand, model, storage, battery)
        self.camera_megapixels = camera_megapixels
    
    # New method unique to SmartphoneWithCamera
    def take_photo(self):
        if self.is_on:
            print(f"Taking a photo with {self.camera_megapixels}MP camera.")
        else:
            print("Please turn on the phone to take a photo.")

# Usage
phone = Smartphone("Samsung", "Galaxy S20", 128, 75)
phone.power_on()
phone.charge(15)

camera_phone = SmartphoneWithCamera("Apple", "iPhone 14", 256, 50, 12)
camera_phone.power_on()
camera_phone.take_photo()
camera_phone.power_off()



#Activity 2: Polymorphism Challenge with Vehicles

# Base Class: Vehicle
class Vehicle:
    def move(self):
        pass  # Abstract method (to be overridden by derived classes)

# Derived Class: Car
class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

# Derived Class: Plane
class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

# Derived Class: Boat
class Boat(Vehicle):
    def move(self):
        print("Sailing 🚤")

# Testing Polymorphism
vehicles = [Car(), Plane(), Boat()]

for vehicle in vehicles:
    vehicle.move()  # Calls the move method specific to each vehicle type

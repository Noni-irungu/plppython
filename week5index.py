#Assignment 1
# Define a base class for a generic Device
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def device_info(self):
        return f"Device: {self.brand} {self.model}"

# Define a derived class for a Smartphone
class Smartphone(Device):
    def __init__(self, brand, model, storage, camera_megapixels):
        super().__init__(brand, model)
        self.storage = storage
        self.camera_megapixels = camera_megapixels

    def smartphone_info(self):
        return f"{self.device_info()}, Storage: {self.storage}GB, Camera: {self.camera_megapixels}MP"

    def take_photo(self):
        return f"{self.brand} {self.model} is taking a photo with its {self.camera_megapixels}MP camera!"

# Define another derived class for a Laptop
class Laptop(Device):
    def __init__(self, brand, model, ram, processor):
        super().__init__(brand, model)
        self.ram = ram
        self.processor = processor

    def laptop_info(self):
        return f"{self.device_info()}, RAM: {self.ram}GB, Processor: {self.processor}"

    def code(self):
        return f"{self.brand} {self.model} is running a Python script!"

# Example usage
if __name__ == "__main__":
    phone = Smartphone("Apple", "iPhone 14", 128, 12)
    laptop = Laptop("Dell", "XPS 15", 16, "Intel i7")

    print(phone.smartphone_info())
    print(phone.take_photo())

    print(laptop.laptop_info())
    print(laptop.code())


#Assignment 2: Polymorphism
# Define a base class for a generic Vehicle
class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method")

# Define a derived class for a Car
class Car(Vehicle):
    def move(self):
        return "Driving 🚗"

# Define a derived class for a Plane
class Plane(Vehicle):
    def move(self):
        return "Flying ✈️"

# Define a derived class for a Boat
class Boat(Vehicle):
    def move(self):
        return "Sailing 🚤"

# Example usage
if __name__ == "__main__":
    vehicles = [Car(), Plane(), Boat()]

    for vehicle in vehicles:
        print(vehicle.move())
# Assignment 1: Design Your Own Class! 🏗️

# Smartphone class
class Smartphone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
    
    # Method to make a call
    def call(self, number):
        print(f"Calling {number}...")
    
    # Method to browse the internet
    def browse(self, website):
        print(f"Browsing {website}...")
    
    # Method to play music
    def play_music(self, song):
        print(f"Playing {song}...")
    
    # Method to display phone details
    def display_details(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Price: {self.price}")


# Inherited Smartphone class with Camera
class SmartphoneWithCamera(Smartphone):
    def __init__(self, brand, model, price, camera_quality):
        super().__init__(brand, model, price)
        self.camera_quality = camera_quality
    
    # Method to take a photo
    def take_photo(self):
        print(f"Taking a photo with {self.camera_quality} quality camera.")

# Creating an instance of Smartphone
my_phone = Smartphone("Apple", "iPhone 13", 999)
my_phone.display_details()  # Display the details
my_phone.call("123-456-7890")  # Make a call
my_phone.browse("www.example.com")  # Browse the internet
my_phone.play_music("Shape of You")  # Play music

# Creating an instance of SmartphoneWithCamera
my_phone_with_camera = SmartphoneWithCamera("Samsung", "Galaxy S21", 899, "108 MP")
my_phone_with_camera.display_details()  # Display the details
my_phone_with_camera.take_photo()  # Take a photo


# Activity 2: Polymorphism Challenge! 🎭

# Vehicle class (Base class)
class Vehicle:
    def move(self):
        pass  # Placeholder method

# Car class (Inherited from Vehicle)
class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

# Plane class (Inherited from Vehicle)
class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

# Creating instances of Car and Plane
car = Car()
plane = Plane()

# Calling move() for both
car.move()  # Output: Driving 🚗
plane.move()  # Output: Flying ✈️

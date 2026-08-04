class Vehicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed
    def info(self):    
        print(f"{self.brand} can go {self.speed} km/h.")

class Car(Vehicle):
    def __init__(self, brand, speed, model):
        super().__init__(brand, speed)
        self.model = model
    def info(self):
        super().info()
        print(f"{self.brand} {self.model} can go {self.speed} km/h and has 4 doors.")        

c1 = Car("Toyota", 180, "Camry")
c1.info()        
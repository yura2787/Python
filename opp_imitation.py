from abc import ABC, abstractmethod

class Vehicle(ABC):

    def __init__(self, brand: str, model: str):
        self.brand = brand
        self.model = model

    @abstractmethod
    def info(self):
         pass

class Car(Vehicle):
    def __init__(self, num_doors: int, brand: str, model: str):
        self.num_doors = num_doors
        super().__init__(brand, model)

    def info(self):
        print(f'Brand: {self.brand}, Model: {self.model} Num doors: {self.num_doors}')


class Bike(Vehicle):
    def __init__(self, type: str, brand: str, model: str, ):
        self.type = type
        super().__init__(brand, model)

    def info(self):
        print(f'Brand: {self.brand}, Model: {self.model} Type: {self.type}')

class Truck(Vehicle):
    def __init__(self, capacity: int, brand: str, model: str):
        self.capacity = capacity
        super().__init__(brand, model)


    def info(self):
        print(f'Brand: {self.brand}, Model: {self.model} Capacity tons: {self.capacity}')


car = Car(brand='Volkswagen', model='Tiguan', num_doors=4)
bike = Bike(brand='Discovery', model='Trek AM DD ST 26', type='urban')
truck = Truck(brand='MAN', model='TGX', capacity=17)

car.info()
bike.info()
truck.info()

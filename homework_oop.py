class Car:

    def __init__(self, year: int, manufacture: str, model: str, fuel_consumption: float, price: int):
        self.year = year
        self.manufacture = manufacture
        self.model = model

        self.run = 0
        self.fuel_consumption = fuel_consumption
        self.price = price

    def drive(self):
        print(f'Я авто марки {self.manufacture}, їду по справам господаря')

    @property
    def category(self):
        if self.price > 15000:
            print('Крутяк')
        else:
            print('Тачелла')


car = Car(manufacture='Hyundai', model='Santa_fe', year=2012, fuel_consumption=7.8, price=12000)
car.run = 20000
car1 = Car(manufacture='Volkswagen', model='Tiguan', year=2021, fuel_consumption=9.8, price=41716)
car1.run = 57000
car2 = Car(manufacture='Bmw', model='X5', year=2018, fuel_consumption=9.0, price=60000)
car2.run = 101000

car.run = 40000
car.drive()

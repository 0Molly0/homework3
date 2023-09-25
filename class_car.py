class Car:
    def __init__(self, date: int, manufacturer: str, brand: str, fuel_consumption: float):
        self.date = f'Рік випуску = {date}'
        self.manufacturer = f'Виробник {manufacturer}'
        self.brand = f'Mарка {brand}'
        self.fuel_consumption = fuel_consumption
        self.race = 0

    def __str__(self):
        return f'Пробіг = {self.race}'


car_class = Car(date=2020, manufacturer='Toyota', brand='Camry', fuel_consumption=7.1)
car_class_2 = Car(date=2020, manufacturer='Audi', brand='A4', fuel_consumption=5.6)
print(car_class)
print(car_class.date)
print(car_class.manufacturer)
print(car_class.brand)
print(car_class.fuel_consumption)
print(' ')
print(car_class_2.date)
print(car_class_2.manufacturer)
print(car_class_2.brand)
print(car_class_2.fuel_consumption)

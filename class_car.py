import csv


class Car:
    def __init__(self, date: int, manufacturer: str, brand: str, fuel_consumption: float):
        self.date = f'Рік випуску = {date}'
        self.manufacturer = f'Виробник {manufacturer}'
        self.brand = f'Mарка {brand}'
        self.fuel_consumption = f'Витрата палива = {fuel_consumption}'
        self.race = 0
        self.car_file()

    def __str__(self):
        return f'Пробіг = {self.race}'

    def car_file(self):
        with open('car.csv', mode='a', encoding='utf-8') as file:
            writer = csv.writer(file, delimiter='\n')
            writer.writerow([self.brand, self.manufacturer])


class Truck(Car):
    def __init__(self, date: int, manufacturer: str, brand: str, fuel_consumption: float, carrying_capacity: int | float):
        super().__init__(date=date, manufacturer=manufacturer, brand=brand, fuel_consumption=fuel_consumption)
        self.carrying_capacity = f'Bантажопідйомність = {carrying_capacity}'


class SportsCar(Car):
    def __init__(self, date: int, manufacturer: str, brand: str, fuel_consumption: float, maximum_speed: str | float, price: int | float):
        super().__init__(date=date, manufacturer=manufacturer, brand=brand, fuel_consumption=fuel_consumption)
        self.maximum_speed = f'Mаксимальна швидкість = {maximum_speed}'
        self.price = f'Ціна автомобіля = {price}'


# car_class = Car(date=2020, manufacturer='Toyota', brand='Camry', fuel_consumption=7.1)
# car_class_2 = Car(date=2020, manufacturer='Audi', brand='A4', fuel_consumption=5.6)
car_class_truck = Truck(date=2020, manufacturer='Toyota', brand='Camry', fuel_consumption=7.1, carrying_capacity=67.0)
car_class_truck_2 = Truck(date=2020, manufacturer='Audi', brand='A4', fuel_consumption=5.6, carrying_capacity=0)
class_sports_car = SportsCar(date=2020, manufacturer='Toyota', brand='Camry', fuel_consumption=7.1, maximum_speed=0, price=0)
class_sports_car_2 = SportsCar(date=2020, manufacturer='Audi', brand='A4', fuel_consumption=5.6, maximum_speed=0, price=0)
print(
    car_class_truck, '\n',
    car_class_truck.date, '\n',
    car_class_truck.manufacturer, '\n',
    car_class_truck.brand, '\n',
    car_class_truck.fuel_consumption, '\n',
    car_class_truck.carrying_capacity, '\n',
    )
print(
    car_class_truck_2, '\n',
    car_class_truck_2.date, '\n',
    car_class_truck_2.manufacturer, '\n',
    car_class_truck_2.brand, '\n',
    car_class_truck_2.fuel_consumption, '\n',
    car_class_truck_2.carrying_capacity, '\n',
    )
print(
    class_sports_car, '\n',
    class_sports_car.date, '\n',
    class_sports_car.manufacturer, '\n',
    class_sports_car.brand, '\n',
    class_sports_car.fuel_consumption, '\n',
    class_sports_car.maximum_speed, '\n',
    class_sports_car.price, '\n',
    )
print(
    class_sports_car_2, '\n',
    class_sports_car_2.date, '\n',
    class_sports_car_2.manufacturer, '\n',
    class_sports_car_2.brand, '\n',
    class_sports_car_2.fuel_consumption, '\n',
    class_sports_car_2.maximum_speed, '\n',
    class_sports_car_2.price, '\n',
    )

class Transport:
    def __init__(self, the_model, the_year, the_color):
        # attributes/fields
        self.model = the_model
        self.year = the_year
        self.color = the_color

    def change_color(self, new_color):
        print('Changing color...')
        self.color = new_color


class Plane(Transport):
    def __init__(self, the_model, the_year, the_color):
        super().__init__(the_model, the_year, the_color)


class Car(Transport):
    # class attributes
    counter = 0
    wheels_numbers = 4

    # constructor
    def __init__(self, the_model, the_year, the_color, penalties=0):
        # attributes/fields
        super().__init__(the_model, the_year, the_color)
        self.penalties = penalties
        Car.counter += 1

    # method
    def drive(self, city):
        print(f'Car {self.model} is driving to {city}')


class Truck(Car):
    wheels_numbers = 12
    def __init__(self, the_model, the_year, the_color,
                 penalties=0, load_capacity=0):
        super().__init__(the_model, the_year, the_color, penalties)
        self.load_capacity = load_capacity

    def load_cargo(self, weight, type):
        if weight > self.load_capacity:
            print(f'You can not load more than {self.load_capacity} kg.')
        else:
            print(f'Cargo of {type} ({weight} kg.) '
                  f'was successfully loaded on {self.model}')


print(f'We produced {Car.counter} on CARS FABRIC')
price_of_winter_lastic = 5000
print(f'We need {Car.counter * Car.wheels_numbers * price_of_winter_lastic} '
      f'soms to buy winter lastics for our cars')
bmw_car = Car('BMW X6', 2020, 'Black')
print(bmw_car)
print(f'MODEL: {bmw_car.model} YEAR: {bmw_car.year} COLOR: {bmw_car.color} '
      f'PENALTIES: {bmw_car.penalties}')
honda_car = Car(the_year=2009, the_model='Honda CR-V',
                penalties=900, the_color='Silver')
print(f'MODEL: {honda_car.model} YEAR: {honda_car.year} '
      f'COLOR: {honda_car.color} PENALTIES: {honda_car.penalties}')
# honda_car.color = 'Blue'
honda_car.change_color('Blue')
print(f'MODEL: {honda_car.model} YEAR: {honda_car.year} '
      f'NEW COLOR: {honda_car.color} PENALTIES: {honda_car.penalties}')

honda_car.drive('Osh')
bmw_car.drive('Tokmok')
honda_car.drive('Kant')

Car.wheels_numbers = 5
print(f'We produced {Car.counter} on CARS FABRIC')
print(f'We need {Car.counter * Car.wheels_numbers * price_of_winter_lastic} '
      f'soms to buy winter lastics for our cars')

boeing_plane = Plane('Boeing 747', 2022, 'White')
print(f'MODEL: {boeing_plane.model} YEAR: {boeing_plane.year} '
      f'COLOR: {boeing_plane.color}')
boeing_plane.change_color('Green')
print(f'MODEL: {boeing_plane.model} YEAR: {boeing_plane.year} '
      f'NEW COLOR: {boeing_plane.color}')

kamaz_truck = Truck('Kamaz 45', 2000,
                    'Blue', 0, 25000)
kamaz_truck.load_cargo(30000, 'apples')
kamaz_truck.load_cargo(20000, 'potatoes')
kamaz_truck.drive('Batken')

print(f'Truck Factory --> number of wheels: {Truck.wheels_numbers}')

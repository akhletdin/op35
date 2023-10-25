class Contact:
    def __init__(self, city, street, number):
        self.__city = city
        self.__street = street
        self.__number = number

    @property
    def city(self):
        return self.__city

    @city.setter
    def city(self, value):
        self.__city = value

    @property
    def street(self):
        return self.__street

    @street.setter
    def street(self, value):
        self.__street = value

    @property
    def number(self):
        return self.__number


class Animal:
    def __init__(self, name, age, contact):
        self.__name = name
        if type(age) == int and age > 0:
            self.__age = age
        else:
            raise ValueError('Wrong value for age attribute. '
                             'It must be positive number')
        if type(contact) == Contact:
            self.__contact = contact
        else:
            raise ValueError('Wrong value for contact attribute. '
                             'It must be of data type Contact')
        self.__was_born()

    def __was_born(self):
        print(f'Animal {self.__name} was born!')

    def get_age(self):
        return self.__age

    def set_age(self, new_age):
        if type(new_age) == int and new_age > 0:
            self.__age = new_age
        else:
            raise ValueError('Wrong value for age attribute. '
                             'It must be positive number')

    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        self.__name = new_name

    @property
    def contact(self):
        return self.__contact

    def speak(self):
        raise NotImplementedError('Method speak must be implemented')

    def info(self):
        return (f'NAME: {self.__name} AGE: {self.__age} '
                f'BIRTH YEAR: {2023 - self.__age}\n'
                f'CONTACT INFO: {self.contact.city}, '
                f'{self.contact.street} {self.contact.number}')


class Fish(Animal):
    def __init__(self, name, age, contact):
        super(Fish, self).__init__(name, age, contact)

    def speak(self):
        pass


class Cat(Animal):
    def __init__(self, name, age, contact):
        super(Cat, self).__init__(name, age, contact)

    def speak(self):
        print('Myauuu')


class Dog(Animal):
    def __init__(self, name, age, commands, contact):
        super(Dog, self).__init__(name, age, contact)
        self.__commands = commands

    @property
    def commands(self):
        return self.__commands

    @commands.setter
    def commands(self, value):
        self.__commands = value

    def speak(self):
        print('Gav')

    def info(self):
        return super().info() + f'\nCOMMANDS: {self.__commands}'


class FightingDog(Dog):
    def __init__(self, name, age, commands, wins, contact):
        super(FightingDog, self).__init__(name, age, commands, contact)
        self.__wins = wins

    @property
    def wins(self):
        return self.__wins

    @wins.setter
    def wins(self, value):
        self.__wins = value

    def speak(self):
        print('Rrrrr gav')

    def info(self):
        return super().info() + f'\nWINS: {self.__wins}'


# some_animal = Animal('Anim', 2)
# some_animal.set_age(3)
# print(some_animal.info())
# print(some_animal.get_name())

contact_1 = Contact('Bishkek', 'Isanova', 4)
#       a = b

dog = Dog('Sharik', 1, 'Sit', contact_1)
dog.commands = 'Sit, Bark'
print(dog.commands)

fighting_dog = FightingDog('Reks', 3,'Fight', 10, contact_1)

cat = Cat('Murka', 7, Contact('Osh', 'Lenina', 22))

fish = Fish('Nemo', 2, contact_1)

animals_list = [fish, dog, fighting_dog, cat]
for animal in animals_list:
    print(animal.info())
    animal.speak()
    print('----------')

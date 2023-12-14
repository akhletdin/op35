class SuperHero:
    person = "people"

    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase

    def name_hero(self):
        return self.name

    def double_health(self):
        self.health_points = self.health_points * 2

    def __str__(self):
        return f'Имя героя: {self.nickname}, суперспособность: {self.superpower}, ' \
               f'Количество здоровье: {self.health_points}'

    def __len__(self):
        return len(self.catchphrase)


superman = SuperHero("Clark Kent", "Superman", "Flight and super strength", 100, "Up, up and away!")

hero_name = superman.name_hero()
print(f"Прозвище героя: {hero_name}")

print(superman)
superman.double_health()
print(f"Здоровье героя удвоено: {superman.health_points}")


print(f"Длина коронной фразы героя: {superman.__len__()}")

def apply_super_power(self, boss, heroes):
    boost_point = randint(5, 11)
    print(f"Boost: {boost_point}")
    for hero in heroes:
        if hero.health > 0 and hero != self:
            hero.damage += boost_point


class Thor(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, Ability.STUN)

    def apply_super_power(self, boss, heroes):
        stun = [1, 2, 3]
        b = choice(stun)
        if b == 1:
            boss.damage = 0
            print("STUN BOSS")
        else:
            boss.damage = 50


class Witcher(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, Ability.CALL)

    def apply_super_power(self, boss, heroes):
        for hero in heroes:
            if hero.health <= 0 or boss.health > 0:
                hero.health += self.health
                self.health = 0
                print(f"{self.name} пожертвовал собой и возродил  {hero.name}")
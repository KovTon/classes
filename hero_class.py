class Hero():
    def __init__(self,
                 name: str,
                 character_class: str,
                 race: str,
                 hp: int,
                 ag: int,
                 dmg: int,
                 armor: int
                 ):

        self.name = name
        self.character_class = character_class
        self.race = race
        self.hp = hp
        self.ag = ag
        self.money_bag = 0
        self.dmg = dmg
        self.armor = armor
        self.is_defense = False
        self.x = 0
        self.y = 0

    def move_up(self):
        self.y += 1

    def move_down(self):
        self.y -= 1

    def move_left(self):
        self.x += 1

    def move_right(self):
        self.x -= 1

    def get_coin(self, coin):
        self.money_bag += coin

    def get_dmg(self, amount_of_enemy_dmg):
        if self.is_defense:
            amount_of_enemy_dmg -= self.armor
            agility = 50
        else:
            agility = 10
        self.hp -= amount_of_enemy_dmg
        self.ag -= agility

    def defense(self):
        self.is_defense = True

    def stop_defense(self):
        self.is_defense = False

    def attack(self):
        self.ag -= 100
        return self.dmg

    def display_info(self):
        print(f"Имя: {self.name}\n"
              f"Здоровье: {self.hp}\n"
              f"Урон: {self.dmg}\n"
              f"Выносливость: {self.ag}\n")


def main():
    hero = Hero('Diablo', 'bard', 'undead', 100500, 150, 10000, 200)
    oreh = Hero('Nameless', 'warrior', 'skeleton', 900000, 40, 500, 20)

    print('\n1Round_++++++++++++++++++++++++++++++1')
    print(oreh.name, oreh.hp, oreh.ag)
    print(hero.name, hero.hp, hero.ag)
    oreh.get_dmg(hero.attack())
    oreh.defense()
    oreh.get_coin(10)

    print('\n2Round_++++++++++++++++++++++++++++++2')
    print(oreh.name, oreh.hp, oreh.ag)
    print(hero.name, hero.hp, hero.ag)
    oreh.get_dmg(hero.attack())
    oreh.defense()

    print('\n3Round_++++++++++++++++++++++++++++++3')
    print(oreh.name, oreh.hp, oreh.ag)
    print(hero.name, hero.hp, hero.ag)
    hero.get_dmg(hero.attack())
    oreh.get_dmg(oreh.attack())

    print(oreh.name, oreh.hp, oreh.ag)
    print(hero.name, hero.hp, hero.ag)


if __name__ == '__main__':
    main()

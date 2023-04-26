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

    def get_dmg_from(self, amount_of_enemy_dmg):
        self.hp -= amount_of_enemy_dmg
        self.ag -= 10

    def defense_from(self, amount_of_enemy_dmg):
        self.hp = self.hp + self.armor - amount_of_enemy_dmg
        self.ag -= 50

    def attack(self):
        self.ag -= 100
        return self.dmg

    def display_info(self):
        print(f"Имя: {self.name}\n"
              f"Здоровье: {self.hp}\n"
              f"Урон: {self.dmg}\n"
              f"Выносливость: {self.ag}\n")


if __name__ == '__main__': 
     main()

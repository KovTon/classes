class Hero():
    def __init__(self,
                 name: str,
                 character_class: str,
                 race: str,
                 hp: int,
                 ag: int,
                 dmg: int,
                 armor: int,
                 money_bag: int):

        self.name = name
        self.character_class = character_class
        self.race = race
        self.hp = hp
        self.ag = ag
        self.money_bag = money_bag
        self.dmg = dmg
        self.armor = armor

    def get_dmg_and_defended(self, hp, armor, amount_of_dmg):
        if self.ag <= 0:
            print(f"{self.name} can't defense")
            self.hp = hp - amount_of_dmg
        self.hp = self.hp + armor - amount_of_dmg
        self.ag -= 50

    def display_hero_info(self):
        print(f"Имя: {self.name}\n"
              f"Здоровье: {self.hp}\n"
              f"Урон: {self.dmg}\n"
              f"Выносливость: {self.ag}\n")


class Enemy():
    def __init__(self,
                 name: str,
                 character_class: str,
                 race: str,
                 hp: int,
                 ag: int,
                 dmg: int,
                 armor: int,
                 money_bag: int):

        self.name = name
        self.character_class = character_class
        self.race = race
        self.hp = hp
        self.ag = ag
        self.money_bag = money_bag
        self.dmg = dmg
        self.armor = armor


# def hero_get_dmg(actor_1, actor_2):
#     actor_1 = 
#     return hero.hp = actor_1 - actor_2

hero = Hero('Diablo', 'bard', 'undead', 100500, 150, 10000, 200, 0)
enemy = Enemy('Nameless', 'warrior', 'skeleton', 900000, 40, 500, 20, 25)
print(hero.name, hero.character_class)
print(hero.hp - enemy.dmg)
print('1++++++++++++++++++++++++++++++1')

# а если через функцию 'def hero_get_dmg_and_defended'?
print(hero.display_hero_info())

print(hero.name, hero.hp, hero.ag)
hero.get_dmg_and_defended(hero.hp, hero.armor, enemy.dmg)
print(hero.name, hero.hp, hero.ag)
hero.get_dmg_and_defended(hero.hp, hero.armor, enemy.dmg)
print(hero.name, hero.hp, hero.ag)
hero.get_dmg_and_defended(hero.hp, hero.armor, enemy.dmg)
print(hero.name, hero.hp, hero.ag)
hero.get_dmg_and_defended(hero.hp, hero.armor, enemy.dmg)
print(hero.name, hero.hp, hero.ag)
hero.get_dmg_and_defended(hero.hp, hero.armor, enemy.dmg)

#есть проблема. Enemy наносит урон по 700, а должен по 500.

print(hero.display_hero_info())

# Изменил '-' на '+' в функции. Стал не по 700, а по 300. 
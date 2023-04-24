class Hero():
    def __init__(self, name: str, character_class: str, race: str, HP: int, AG: int, money_bag: int):
        self.name = name
        self.character_class = character_class
        self.race = race
        self.HP = HP
        self.AG = AG
        self.money_bag = money_bag
        
    def movement():
        pass


hero = Hero('Diablo', 'bard', 'undead', 100500, 70, 0)

print(hero.name)

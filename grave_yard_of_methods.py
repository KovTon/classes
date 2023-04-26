# Метод хранит простые механики слабости и агонии. Он сам лишь напоминание о 
# том что в одном методе два действия не надо реализовывать. Но и данных он
# требует много.

def get_dmg_and_defended(self, hp, armor, amount_of_dmg):
    if self.ag <= -200:
        print(f"{self.name} can't defense, he is in agony")
        self.hp = hp - amount_of_dmg * 2
    if self.ag <= 0:
        print(f"{self.name} can't defense")
        self.hp = hp - amount_of_dmg
    self.hp = self.hp + armor - amount_of_dmg
    self.ag -= 50
    
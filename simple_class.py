def not_function():
    pass


class Car():
    def input_label(self, label: str):
        self.label = label

    def __init__(self, label: str, volume: int):
        self.label = label
        self.volume = volume
        self.cargo = None

    def load(self, cargo: str):
        self.cargo = cargo

    def unload(self):
        hands = self.cargo
        self.cargo = None
        return hands

    @staticmethod
    def get_factory():
        return "gear motors"


result = not_function()
car1 = Car('porsche', 3)
car2 = Car('ferrari', 4)

car1.input_label('porsche')
# car2.input_label('ferrari')

# car1.label = 'porsche'
print(car1.label, car1.cargo)
print(car2.label)
car1.load('orange')
car2.load('apples')
print(car1.label, car1.cargo)
print(car1.unload())
print(car1.label, car1.cargo)

print(car1.get_factory())
print(car2.get_factory())

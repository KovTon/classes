class Car():
    """Простая модель автомобиля."""
    def __init__(self, make, model, year):
        """Инициализирует атрибуты описания автомобиля."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        self.gas_tank_volume = 0

    def get_descriptive_name(self):
        """Возвращает аккуратно отформатированное описание."""
        long_name = str(self.year).title() + ' ' + self.make + ' ' + self.model
        return long_name

    def read_odometer(self):
        """Выводит пробег машины в милях."""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        """
        Устанавливает на одометре заданное значение.
        При попытке обратной подкрутки изменение отклоняется.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Увеличивает показания одометра с заданным приращением."""
        self.odometer_reading += miles

    def fill_gas_tank(self):
        """У электромобилей нет бензобака."""
        return "This car doesn't need a gas tank!"


class ElectricCar(Car):
    """Представляет аспекты машины, специфические для электромобилей."""
    # [ ] Стоит ли в доке писать, что это наследник от Car?
    def __init__(self, make, model, year):
        """Инициализирует атрибуты класса-родителя."""
        super().__init__(make, model, year)
        # [ ] на стр.172 всратый indentation?
        self.battery = Battery()

    def describe_batter(self):
        '''Возвращает строку с информацией о мощности аккумулятора.'''
        # [ ] как-то Battery надо "полечить". Хочу в плейсхолдере держать ее.
        return f"This car has a {self.battery} -kWh battery."

    def fill_gas_tank(self):
        """У электромобилей нет бензобака."""
        return f"{self.make.title()} {self.model.title()} doesn't need a gas!"


class Battery():
    """Простая модель аккумулятора электромобиля."""
    def __init__(self, battery_size=70):
        """Инициализирует атрибуты аккумулятора."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Выводит информацию о мощности аккумулятора."""
        return f"This car has a {self.battery_size} -kWh battery."

    # def get_range(self):
    #     #   [ ] не получается нормально вывести значение. выдает 0.
    #     """Выводит приблизительный запас хода для аккумулятора."""
    #     range = 0
    #     # [ ] а можно без создания переменной range до условной конструкции,
    #     # но с помощью хитрого некоего format?
    #     message = f"This car can go approximately {range} miles on a full charge."
    #     if self.battery_size == 70:
    #         range = 240
    #     elif self.battery_size == 85:
    #         range = 270 
    #     return message

    def get_range(self):
        """Выводит приблизительный запас хода для аккумулятора."""
        # range = 0
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        # [ ]Прога не понимает что переменная будет создана?
        # Той часть которая подчеркивает, не известно компилируещей???
        return f"This car can go approximately {range} miles on a full charge."


my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()
my_new_car.odometer_reading = 23
my_new_car.read_odometer()
# [ ]не может прицепить метод к методу
# my_new_car.update_odometer(23000).increment_odometer(100)
my_new_car.read_odometer()


tesla_hoover_X5000 = ElectricCar('tesla', 'model s', 2016)
print(tesla_hoover_X5000.get_descriptive_name())
# [ ] не показывает значение.Понял. Потому что метод/функцию battery не трогал.
# А как правильно сказать-то предыдущее предложение?
print(tesla_hoover_X5000.describe_batter())
print(tesla_hoover_X5000.fill_gas_tank())
print(tesla_hoover_X5000.battery.describe_battery())
# [ ] выдает неправильные значения у моего варианта кода.
print(tesla_hoover_X5000.battery.get_range())
batarika = Battery(100)
print(tesla_hoover_X5000.battery.get_range())

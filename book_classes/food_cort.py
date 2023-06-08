class Restaurant():
    def __init__(self, restaurant_name: str, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        # [ ] не подсвечивается, но работает title() Решил - указал тип
        # restaurant в __init__ .
        print(self.restaurant_name.title(), self.cuisine_type)

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open")

    def increment_number_served(self, clients):
        self.number_served += clients

    # def set_number_served(self, served_clients):
    #     self.


# 9-2.165 Создал три экземпляра и вызвал метод describe_restaurant
u_givi = Restaurant("u Givi", "georgian")
tuda_suda = Restaurant("tuda-suda", "korean")
porka_putana = Restaurant("rest for aunt", "italian")


restaurants = [u_givi, tuda_suda, porka_putana]
for restaurant in restaurants:
    restaurant.describe_restaurant()
    # [ ]TODO: откуда взялся None. Нашел - принт принта дает None.

print(u_givi.number_served)
u_givi.number_served = 333
print(u_givi.number_served)
u_givi.increment_number_served(222)
print(u_givi.number_served)


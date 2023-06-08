class User():
    def __init__(self, first_name, last_name) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.friends = []
        self.login_attempts = 0

    def get_amount_friends(self) -> int:
        ''' считает количество друзей '''
        return len(self.friends)

    def add_friend(self, friend: 'User'):
        '''добавляет друга и сообщает о добавлении'''
        self.friends.append(friend)
        return f'{friend.first_name} was added'

    def v2_greet_user(self):
        # [ ] Такое вложение метода в тело другого метода норм?
        # Я читал только про вызов функции самой функцией.
        # [ ] Можно ли сделать вывод, что ему пофиг? Я вызвал(?) метод до его
        # инициализации(норм сказал)? Наверное ответ в компиляции, исполнении
        # и прочих состояних выполнения текста.
        return f"Greetings, {User.describe_user(self).title()}"

    def describe_user(self):
        return f'{self.first_name} {self.last_name}'

    def v1_greet_user(self):
        # [ ] что-то настораживает print и как-то describe_user похож на
        # greet_user
        return f"Greetings, {self.first_name}  {self.last_name}"

    def increment_login_attempts(self):
        '''увеличивает значение попыток залогиниться'''
        self.login_attempts += 1

    def reset_login_attempts(self):
        ''' обнуляет значение попыток залогиниться'''
        self.login_attempts = 0

#[ ] я хотел не назначая каждый экземпляр бахнуть сразу их список
# users: list[User] = [tinki-winky, lala, po]


tinki_winky = User('tinki-winky', 'puzik')
lala = User('lala', 'puzik')
po = User('po', 'puzik')

print(lala.v2_greet_user())
print(lala.v1_greet_user())

lala.increment_login_attempts()
lala.increment_login_attempts()
lala.increment_login_attempts()
lala.increment_login_attempts()
lala.increment_login_attempts()
attempts = lala.login_attempts
lala.reset_login_attempts()
print(f'Сейчас значение равно 5? {attempts} Обнулим {lala.login_attempts}')

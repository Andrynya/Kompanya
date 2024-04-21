class User():
    def __init__(self, id, name, lvl="user"):
        self.__id = id
        self.__name = name
        self.__lvl = lvl

    def get_id(self):
        return self.__id #Возможность отображения

    def get_name(self):
        return self.__name

    def get_lvl(self):
        return self.__lvl

class Admin(User):
    def __init__(self, id, name, lvl="admin"):
        super().__init__(id, name, lvl)
        self.users_list = []

    def add_user(self, user):
        self.users_list.append(user) #Добавление в список

    def remove_user(self, user_id):
        for user in self.users_list:
            if user.get_id() == user_id:
                self.users_list.remove(user)
                return #Удаление из списка

    def get_users_list(self):
        return self.users_list #Отображение списка

#Пример вывода информации
admin = Admin(1, "Андрей")

user1 = User(2, "Виктория")
user2 = User(3, "Павел")
user3 = User(4, "Мария")

admin.add_user(user1)
admin.add_user(user2)
admin.add_user(user3)

print("Список пользователей:")
for user in admin.get_users_list():
    print(user.get_name())

admin.remove_user(2)

print("Список пользователей:")
for user in admin.get_users_list():
    print(user.get_name())


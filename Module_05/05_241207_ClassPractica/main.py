class Database():
    def __init__(self):
        self.data = set()

    def show_data(self):
        for data_item in self.data:
            print(data_item)


class User():
    def __init__(self, username, name, age, city, password):
        self.username = username
        self.name = name
        self.age = age
        self.city = city
        self.password = password

    def __str__(self) -> str:
        return f'{self.name}, {self.age} y.o., {self.city}'

    def add_to_database(self, database: Database):
        database.data.add(self)


database = Database()

while True:
    user = User(input('username:'), input('name:'), int(
        input('age:')), input('city:'), input('password:'))

    user.add_to_database(database)
    database.show_data()
    print()

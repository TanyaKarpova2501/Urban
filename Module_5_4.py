class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        return object.__new__(cls)

    def __init__(self, name, number_of_floor):
        self.name = name
        self.number_of_floor = number_of_floor



    def __del__(self):
        print(f'{self.name} Снесен, но он остается в истории')




h1 = House("ЖК Горский", 10)
print(House.houses_history)
h2 = House("ЖК Эдем", 20)
print(House.houses_history)
h3 = House("ЖК Аврора", 20)
print(House.houses_history)

del h1
del h2
print(House.houses_history)
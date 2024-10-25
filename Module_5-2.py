class House:
    def __init__(self, name, number_of_floor):
        self.name = name
        self.number_of_floor = number_of_floor

    def __len__(self):
        return self.number_of_floor

    def __str__(self):
        return f"House(Название = {self.name}, количество этажей = {self.number_of_floor})"


h1 = House("ЖК Горский", 10)
h2 = House("Эдем", 15)
print(h1.name, h1.number_of_floor)
print(h2.name, h2.number_of_floor)
print(len(h1))
print(len(h2))
print(str(h1))
print(str(h2))
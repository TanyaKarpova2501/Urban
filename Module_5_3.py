class House:
    def __init__(self, name, number_of_floor):
        self.name = name
        self.number_of_floor = number_of_floor

    def __len__(self):
        return self.number_of_floor

    def __str__(self):
        return (f"House(Название = {self.name}, количество этажей+"
                f" = {self.number_of_floor})")

    def __eq__(self,other):
        return self.number_of_floor == other.number_of_floor
    def __lt__(self,other):
        return (self.number_of_floor < other.number_of_floor),
    def __le__(self,other):
        return (self.number_of_floor <= other.number_of_floor),
    def __gt__(self,other):
        return (self.number_of_floor > other.number_of_floor),
    def __ge__(self,other):
        return (self.number_of_floor >= other.number_of_floor),
    def __ne__(self,other):
        return (self.number_of_floor != other.number_of_floor)
    def __add__(self, value):
        self.value = value
        return (self.number_of_floor + value)
    def __iadd__(self, value):
        self.value = value
        return (self.number_of_floor + value)
    def __radd__(self, valoe):
        self.value = value
        return (self.number_of_floor + value)




h1 = House("ЖК Горский", 10)
h2 = House("ЖК Эдем", 15)
print(h1.name, h1.number_of_floor)
print(h2.name, h2.number_of_floor)
print(len(h1))
print(len(h2))
print(str(h1))
print(str(h2))
print(h1 == h2)
print(h1 < h2)
print(h1 <= h2)
print(h1 > h2)
print(h1 >= h2)
print(h1 != h2)
h1 = h1 + 10
print(h1)
h2 = h2 + 10
print(h2)

from Module_3_3 import value_disc


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
        if isinstance(other, House):
            return self.number_of_floor == other.number_of_floor
        elif isinstance(other, int):
            return self.number_of_floor == other
    def __lt__(self,other):
        if isinstance(other, House):
            return self.number_of_floor < other.number_of_floor
        elif isinstance(other, int):
            return self.number_of_floor < other
    def __le__(self,other):
        if isinstance(other, House):
            return self.number_of_floor <= other.number_of_floor
        elif isinstance(other, int):
            return self.number_of_floor <= other
    def __gt__(self,other):
        if isinstance(other, House):
            return self.number_of_floor > other.number_of_floor
        elif isinstance(other, int):
            return self.number_of_floor > other
    def __ge__(self,other):
        if isinstance(other, House):
            return self.number_of_floor >= other.number_of_floor
        elif isinstance(other, int):
            return self.number_of_floor >= other
    def __ne__(self,other):
        if isinstance(other, House):
            return self.number_of_floor != other.number_of_floor
        elif isinstance(other, int):
            return self.number_of_floor != other

    def __add__(self, value):
        if isinstance(value, House):
            self.number_of_floor += value
            return self
        elif isinstance(value, int):
            self.number_of_floor += value
            return self
    def __iadd__(self, value):
        self.__add__(value)
        return self
    def __radd__(self, valoe):
        self.__add__(value)
        return self




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
h1 += 10
print(h1)
h2 = h2 + 10
print(h2)

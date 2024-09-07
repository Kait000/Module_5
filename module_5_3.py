class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __eq__(self, other):  # ==
        return self.number_of_floors == other.number_of_floors

    def __lt__(self, other):  # <
        return self.number_of_floors < other.number_of_floors

    def __le__(self, other):  # <=
        return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):  # >
        return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):  # >=
        return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):  # !=
        return self.number_of_floors != other.number_of_floors

    def __add__(self, other):   # x+10
        self.number_of_floors += other
        return self

    def __radd__(self, other):  # 10+x
        return self.__add__(other)

    def __iadd__(self, other):  # +=
        return self.__add__(other)

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

    def __len__(self):
        return self.number_of_floors

    def go_to(self, new_floor):
        if 0 < new_floor <= self.number_of_floors:
            for i in range(new_floor):
                print(i + 1)
        else:
            print('Такого этажа не существует')


h1 = House('Воробьёвы горы', 12)
h2 = House('ЖК Олимпийский', 21)

print(h1)
print(h2)

print(h1 == h2)     # __eq__
h1 = h1 + 9         # __add__
print(h1)
print(h1 == h2)

h1 += 10            # __iadd__
print(h1)

h2 = 10 + h2        # __radd__
print(h2)

print(h1 > h2)      # __gt__
print(h1 >= h2)     # __ge__
print(h1 < h2)      # __lt__
print(h1 <= h2)     # __le__
print(h1 != h2)     # __ne__

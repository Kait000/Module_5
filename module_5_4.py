class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        return object.__new__(cls)

    def __del__(self):
        print(f'{self.name} снесён, но он останется в истории')
        del self

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __eq__(self, other):  # ==
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors == other

    def __lt__(self, other):  # <
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors < other

    def __le__(self, other):  # <=
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors <= other

    def __gt__(self, other):  # >
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors > other

    def __ge__(self, other):  # >=
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors >= other

    def __ne__(self, other):  # !=
        if isinstance(other, House):
            return self.number_of_floors != other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors != other

    def __add__(self, other):   # x+10
        if isinstance(other, House):
            self.number_of_floors += other.number_of_floors
        if isinstance(other, int):
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
print(House.houses_history)
h2 = House('ЖК Олимпийский', 21)
print(House.houses_history)
h3 = House('ЖК Восточный 1', 18)
print(House.houses_history)

del h2
del h3

print(House.houses_history)

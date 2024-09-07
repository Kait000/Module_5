class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

    def __len__(self):
        return self.number_of_floors

    def go_to(self, new_floor):
        if 0 < new_floor <= self.number_of_floors:
            for i in range(new_floor):
                print(i+1)
        else:
            print('Такого этажа не существует')


h1 = House('Воробьёвы горы', 12)
h2 = House('ЖК Олимпийский', 21)

print(h1)
print(h2)

print(len(h1))
print(len(h2))

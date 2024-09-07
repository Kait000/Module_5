class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if 0 < new_floor <= self.number_of_floors:
            for i in range(new_floor):
                print(i+1)
        else:
            print('Такого этажа не существует')


h1 = House('Воробьёвы горы', 12)
h2 = House('ЖК Олимпийский', 21)
h1.go_to(3)
h2.go_to(22)

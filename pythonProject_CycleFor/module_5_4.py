class House:
    houses_history = []
    def __init__(self,name,number_of_floors):
        self.name=name
        self.number_of_floors = number_of_floors
        if isinstance(number_of_floors, House):
            self.houses_history = number_of_floors.append()
    def go_to(self,new_floor):
        if 1 <= new_floor <= self.number_of_floors:
            for floor in range(1,new_floor + 1):
                print(floor)
            else:
                print("Такого этажа не существует")
    def __new__(cls, *args, **kwargs):
        wen = object.__new__(cls)
        args = args[0]
        cls.houses_history.append(args)
        return wen
    def __del__(self):
        return print(f'{self.name} снесён, но он останется в истории')

h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)
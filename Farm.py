class Pets:
    name = "кличка"
    weight = 0
    def feed(self):
        self.state = 'full'

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __gt__(self, other):
        return self.weight > other.weight

class Ungulata:
    def milk(self):
        self.state = 'milked'

class Bird:
    def get_eggs(self):
        self.state = 'fullbasket'

class Goose(Pets, Bird):
    def voice(self):
        self.state = 'cackle'

class Cow(Pets, Ungulata):
    def voice(self):
        self.state = 'Moo'

class Sheep(Pets):
    def trim(self):
        self.state = 'trimmed'
    def voice(self):
        self.state = 'bleat'


class Chiken(Pets, Bird):
    def voice(self):
        self.state = 'cluck'

class Goat(Pets, Ungulata):
    def voice(self):
        self.state = 'bleat'


class Duck(Pets, Bird):
    def voice(self):
        self.state = 'quack'


goose1 = Goose(name="Серый", weight=10)
goose1.feed()
goose1.get_eggs()

goose2 = Goose(name="Белый", weight=15)
goose2.feed()
goose2.get_eggs()

cow1 = Cow(name="Манька", weight=250)
cow1.feed()
cow1.milk()

sheep1 = Sheep(name="Барашек", weight=50)
sheep1.feed()
sheep1.trim()

sheep2 = Sheep(name="Кудрявый", weight=55)
sheep2.feed()
sheep2.trim()

chiken1 = Chiken(name="Ко-Ко", weight=2)
chiken1.feed()
chiken1.get_eggs()

chiken2 = Chiken(name="Кукареку", weight=3)
chiken2.feed()
chiken2.get_eggs()

goat1 = Goat(name="Рога", weight=25)
goat1.feed()
goat1.milk()

goat2 = Goat(name="Копыта", weight=30)
goat2.feed()
goat2.milk()

duck1 = Duck(name="Кряква", weight=4)
duck1.feed()
duck1.get_eggs()

pets_list = [goose1.__dict__, goose2.__dict__, cow1.__dict__,sheep1.__dict__, sheep2.__dict__, chiken1.__dict__, chiken2.__dict__,goat1.__dict__, goat2.__dict__, duck1.__dict__]

all_pets_weight = []

for pet in pets_list:
  all_pets_weight.append(pet['weight'])



print(f'Общий вес всех животных: {sum(all_pets_weight)}')

for pet in pets_list:
    if pet['weight'] == max(all_pets_weight):
        print('Самое тяжелое животное - ', pet['name'], 'весит: ', max(all_pets_weight))



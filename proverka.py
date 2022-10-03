# 2) Реализовать поиск по полям: рост больше 120, имя Наташа
from pprint import pprint


class Person:
    def __init__(self, name, age, address, rost):
        self.name, self.age, self.address, self.rost = name, age, address, rost
        self.key = (name, rost)

    def __rept__(self):
        return "Person('%s', '%s', '%s', '%s')" % (self.name, self.age, self.address, self.rost)

    def __eq__(self, obj):
        return True


lena = Person("Лена", 20, "Мировая, 30, 228", 160)
oleg = Person("Олег", 25, "Кулинарная, 555, 8", 180)
natasha = Person("Наташа", 30, "Мировая, 30, 55", 165)
anton = Person("Антон", 21, "Колотушкина, 28, 666", 176)
peolpe = {
    lena.key: lena,
    oleg.key: oleg,
    natasha.key: natasha,
    anton.key: anton,
}
pprint(peolpe)
pprint(peolpe[anton.key])

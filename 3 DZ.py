# 1) Сделать int такой что 2 + 2 = 5

class MyInt(int):
    def __add__(self, x):
        return super().__add__(x + 1)


y = MyInt(2)

# 2) Сделать лист такой что больше 10 нельзя


class MyList(list):
    def __init__(self, x):
        if len(x) > 10:
            raise ValueError('> 10')
        else:
            super().__init__(x)

    def append(self, x):
        if len(self) == 10:
            raise ValueError('> 10')
        else:
            super().append(x)


y = MyList([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# 3) Сделать лист с уникальными элементами


class MyList(set):
    pass


y = MyList([1, 1, 2, 2, 3, 3])
y = {1, 2, 3}

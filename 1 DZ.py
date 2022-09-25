# Сумма числел от 0 до 10
print(sum(range(10)))

# Произведение их на 2
for i in range(10):
    print(i * 2)

# Средний возраст в адитории
ages = [18, 19, 20, 21, 22, 17, 22, 25, 30, 24]
print(sum(ages)/len(ages))

# Состав семьи
family = {
    'Father': 'Viktor',
    'Mother': 'Anastasia',
    'Son': 'Evgenii',
    'Daughter': 'Alina'
}
# Вывести имя отца
print(family['Father'])

# Cостав группы
sostav_group = (('Sasha', 23), ('Masha', 18), ('Ekaterina', 22),
                ('Fasol', 25), ('Nikola', 30), ('Mikola', 27))

# Вывести имя и возраст третьего по списку из группы
print(sostav_group[2])

# Зачётная книжка студента
Maksim_NGD_20_1b = [
    ['НГПО', 5, ],
    ['Высшая математика', 5, ],
    ['СНГС', 5, ],
    ['Информатика', 5, ],
]

# Вывести оценку по первому предмету
print(Maksim_NGD_20_1b[0])

import math

# Задание 1
x = float(input('Укажите любое число:'))
number = int(x)
sum = (number * (number + 1))/2
print(f'Задача 1. Итого: {sum} ')

# Задание 2
a = int(input('первое число:'))
b = int(input('второе число:'))
print(f'Арифмитические:\n'
      f'сумма- {a + b}\n'
      f'разница- {a - b}\n'
      f'произведение- {a * b}\n'
      f'деление- {a / b:.2f}\n'
      f'частное от деления- {a // b}\n'
      f'остаток от деления- {a % b}\n'
      f'десятичный логарифм- {math.log10(a):.2f}\n'
      f'возведение в степень- {a ** b}'
      )
print(f'Cравнение:\n'
      f'больше - {a < b}\n'
      f'больше или равно - {a <= b}\n'
      f'меньше - {a > b}\n'
      f'меньше или равно- {a >= b}\n'
      f'не равно - {a != b}\n'
      f'равно - {a == b}\n'
      )

# Задание 3
x = int(input('x='))
y = int(input('y='))
z = int(input('z='))

f = round((((x ** 5 + 7)/(abs(-6) * y)) ** (1./3.)) / 7 - z % y, 3)
print(f)

# Задание 4
a = float(input('Введите сопротивление 1 проводника: '))
b = float(input('Введите сопротивление 2 проводника: '))
c = round(a + b, 1)
print(f"общее сопротивление цепи: {c}")

# Задание 5
a = float(input('Введите число a: '))
b = float(input('Введите число b: '))
x = -b/a
print(x)
m = float(input('Введите число m: '))
n = float(input('Введите число n: '))
x = x >= m and x <= n
print(x)

# Задание 6
v = int(input('Введите cкорость: '))
t = int(input('Введите время: '))
x = v * t
y = x % 123
z = x//123
s = tuple(range(123))
print(s[y*(-1)**z])

# Задание 7
a = list(input('Введите двухзначное число: '))

xa = int(a[0]) + int(a[1])
ya = int(a[0]) * int(a[1])

b = list(input('Введите трехзначное число: '))
xb = int(b[0]) + int(b[1]) + int(b[2])
yb = int(b[0]) * int(b[1]) * int(b[2])

print(f'Сумма элементов двухзначного числа: {xa}\nПроизведение элементов двухзначного числа: {ya}')
print(f'Сумма элементов трехзначного числа: {xb}\nПроизведение элементов трехзначного числа: {yb}')

# Задание 8
a = int(input('Введите целое число: '))
b = int(input('Введите целое число: '))
c = int(input('Введите целое число: '))

x = min(a, b, c)
y = max(a, b, c)
z = a + b + c - max(a, b, c) - min(a, b, c)
print(x, z, y)

# Задание 9

a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
print(a, b)
a = a + b
b = a - b
a = a - b
print(a, b)

# Задание 10
a = input('Введите название футбольной команды: ')
print(f"{a} - чемпион!")
b = len(a)
print("-" * b)
c = a.lower()
print(len(c), bool(c.find("п")), c.count("а"))

# Задание 11
a = input('Введите название государства: ')
b = input('Введите название его столицы: ')

print(f"Государство - {a}, столица - {b}")

# Задание 12
a = "объектно-ориентированный"
print(a[0:6])
print(a[9:17])
print(a[-10:-7])
print(a[4:15:5])
print(a[10:11]+a[12:15]+a[-5:-4])

# Задача 13
a = []
b = []
a.append(4.5)
a.append(3.4)
a.extend([8.7, 1.3])
b.append(14.5)
b.append(3.4)
b.extend([8.7, 11.3])
a.insert(1,100)
a.insert(3,100)
b.insert(0,200)
b.insert(2,200)
print("Исходные списки:")
print(a)
print(b)
del a[0]
del b[0]
a.remove(100)
b.remove(200)
print("\nПосле удалений:")
print(a)
print(b)

sa = set(a)
sb = set(b)
sa_and_sb = sa&sb
print("\nУникальные элементы:")
print(sa)
print(sb)
print("общие:", sa_and_sb)

c = a + b
c_asc = sorted(c)
c_desc = sorted(c, reverse=True)
print(c)
print(c_asc)
print(c_desc)

chet = c[1::2]
count1 = len(chet)
summ1 = sum(chet)
sr_ar = summ1/count1

c_max = max(c)
c_min = min (c)

nechet = c[::2]
count2 = len(nechet)
prod = int(math.prod(nechet))
sr_geom = round(pow(prod, (1/count2)),3)
print("\nИтоговые:")
print("3-й:", c)
print(sr_ar)
print(sr_geom)
print(c_max)
print(c_min)

# Задание 14
info = dict()
info["фио"] = "Дарья Кирилловна Колесниченко"
info["дата_рождения"] = "05.09.1997"
info["место_рождения"] = "Нижний Новгород"
a = ["Читать книги", "Смотреть сериалы"]
info["Хобби"] = a
a.append("Программирование")
info["животные"] = ("Кошка Буся",
                    "Собака Порши")
info["ЕГЭ"] = dict()
info["ЕГЭ"] = {"Математика": 90,
               "Физика": 85,
               "Информатика": 93}
info["ЕГЭ"]["Обществознание"] = 10
del info["ЕГЭ"] ["Обществознание"]
info ["вузы"] = dict()
info ["вузы"] = {"МГУ": 267,
                 "ВШЭ": 278,
                 "РАНХИГС": 265}
print("Данные:")
print(info)

exams = sorted(info["ЕГЭ"].keys()[0])
print("Предметы:", exams)
uni = sorted(info["вузы"])
print("Вузы:", uni)

print("\nОтветы на вопросы:")
name = {info["фио"][0]}
vowel = {"А", "Е", "Ё", "И", "О", "У", "Ы", "Э", "Ю", "Я"}
starts_with_vowel = name <= vowel
print("* мое имя начинается на гласную букву:", starts_with_vowel)

month = {info["дата_рождения"][3:5]}
winter_summer = {"06", "07", "08","12", "01", "02"}
born_in_winter_or_summer = month <= winter_summer
print("* родился летом или зимой:", born_in_winter_or_summer)

hobbies_count = len(info["Хобби"])
print("* у меня {} хобби, первое {}".format(hobbies_count, info["Хобби"][0]))

print("* после окончания школы сдавал {} экз.".format(len(info["ЕГЭ"])))

sum_mark = sum(info["ЕГЭ"].values())
print("* сумма баллов = {}".format(sum_mark))

max_mark = max(info["ЕГЭ"].values())
print("* макс. балл = {}".format(max_mark))

vuz_count = (int(sum_mark >= list(info["вузы"].values())[0]) +
             int(sum_mark >= list(info["вузы"].values())[1]) +
             int(sum_mark >= list(info["вузы"].values())[2]))
print("* кол-во вузов в которые прохожу: {}".format(vuz_count))




# Задание 1
a = [1, 5, 3]
b = [1, 5, 1, 5]
c = [1, 3, 1, 5, 3, 3]
a.extend(b)
print(a.count(5))
for i in a:
    if i == 5:
        a.remove(5)
a.extend(c)
print(a.count(3))
print(a)

# Задание 2
a = list(range(160, 172, 2))
print(a)
b = list(range(162, 180, 3))
print(b)
new = sorted(a + b)
print(new)

# Задание 3
shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300], ['педаль', 100],
        ['седло', 1500], ['рама', 12000], ['обод', 2000],
        ['шатун', 200], ['седло', 2700]]

a = input('Название детали: ').lower()
price = 0
count = 0
print(a)

for i in shop:
    if a == i[0]:
        count += 1
        price += i[1]
print(f'Кол-во деталей - {count}\nОбщая стоимость - {price}')

# Задание 4
guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']

while True:
    print(f"Сейчас на вечеринке {len(guests)} человек:{guests}")
    a = input("Гость пришел или ушел? ")
    if a == "пришел":
        name = input("Имя гостя?")
        if len(guests)<6:
            guests.append(name)
        else:
            print(f"Прости, {name}, но мест нет.")
    elif a == "ушел":
        name = input("Имя гостя?")
        guests.remove(name)
        print(f"Пока, {name}!")
    elif a == "Пора спать".lower():
        print("Вечеринка закончилась, все легли спать")
        break

# Задание 5
violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]

n = int(input("Сколько песен выбрать? "))

time = 0
play_list = []
for j in range(n):
    name = input(f"Название {j+1}-й песни: ")
    for i in violator_songs:
        if i[0] == name:
            play_list.append(name)
            time += i[1]
print(f"Общее время звучания песен: {time}")

# Задание 6
list1 = []
list2 = []

for i in range(1, 3+1):
    a = int(input(f"Введите {i}-е число для первого списка: "))
    list1.append(a)
for i in range(1, 7+1):
    a = int(input(f"Введите {i}-е число для второго списка: "))
    list2.append(a)

print(f"Первый список: {list1}")
print(f"Второй список: {list2}")

a = list1 + list2
b = set(a)

print(f"Новый первый список с уникальными элементами: {list(b)}")

# Задание 7
n = int(input("Кол-во коньков? "))
m = int(input("Кол-во людей? "))
a = []
b = []
count = 0
for i in range(n):
    con = int(input(f"Размер {i+1}-й пары: "))
    a.append(con)
for j in range(m):
    chel = int(input(f"Размер ноги  {j + 1}-го человека: "))
    b.append(chel)
for i in a:
    if i in b:
        count += 1
        b.remove(i)
print(count)

# Задание 8
n = int(input("Кол-во человек: "))
k = int(input("Какое число в считалке? "))
print(f"Значит, выбывает каждый {k}-й человек")
start = 0
people = list(range(1, n+1))

while len(people) > 1:
    print(f"Текущий круг людей: {people}")
    a = start % len(people)
    print('Начало счёта с номера: ', people[a])
    start = (a + k - 1) % len(people)
    print('Выбывает человек под номером', people[start])
    people.remove(people[start])
print(f"Остался человек под номером {people}")

# Задание 9
n = int(input("Кол-во друзей: "))
k = int(input("Кол-во долговых расписок? "))
sl = dict()

for i in range(1, n+1):
    sl[i] = 0
print(sl)
for i in range(1,k+1):
    print(f"{i}-я расписка")
    a = int(input("Кому:"))
    b = int(input("От кого:"))
    c = int(input("Сколько:"))
    sl[a] -= c
    sl[b] += c
print("Баланс друзей:")
for i, j in sl.items():
    print(f"{i}:{j}")

#Задание 10
n = int(input("Кол-во чисел: "))
a = []
b = []
for i in range(n):
    number = input("Число: ")
    a.append(number)
    b.append(number)
print(f"Последовательность: {a}")

b.reverse()

for i in a:
    while i[-1] == b[0]:
        b.pop(0)


print(f"Нужно приписать чисел: {len(b)}")
print(f"Сами числа: {b}")
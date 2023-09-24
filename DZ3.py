
#Задание 1
n = int(input("Введите количество чисел в списке: "))
nums = [int(input("Введите число: ")) for a in range(n)]
print(nums)

x = int(input("Введите второе число для поиска: "))

for num in nums:
    temp1, temp2 = num, x
    while temp1 != temp2:
        if temp1 < temp2:
            temp2 -= temp1
        else:
            temp1 -= temp2
    nok = int(num * x/temp1)
    print("Числа {} и {}, НОД = {}, НОК = {}".format(num, x, temp1, nok))

#Задание 2

x = str(input("Введите предложения: "))
nums = [0,1,2,3,4,5,6,7,8,9]
count = 0

n = x.split(".")
print(n)

for i in n:
    for j in nums:
        if str(j) in i:
            count += 1
            break

print(count)

#Задание 3
s = str(input("Введите строку: "))
k = str(input("Введите символ: "))

print(f"{k*(len(s)+2)}\n{k+s+k}\n{k*(len(s)+2)}")

#Задание 4
stroc = str(input("Введите предложение: "))
simvol = str(input("Введите символ: "))
count = 0

for i in stroc:
    if i == simvol:
        count += 1

print(f"В строке {stroc} = {count} {simvol}")

#Задание 5
a = str(input("Введите предложение: ")).lower()
alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя" * 2
num = int(input("Введите количество строчек сдвига: "))

def shifr(first_str:str, step:int)->str:
    b = ""
    for i in first_str:
        c = alphabet.find(i)
        new = c + step
        if i in alphabet:
            b += alphabet[new]
        else:
            b += i
    return b

result = shifr(a, num)
def deshifr(second_str:str, step:int)->str:
    b = ""
    for i in second_str:
        c = alphabet.find(i)
        new = c - step
        if i in alphabet:
            b += alphabet[new]
        else:
            b += i
    return b

print(result)
print(deshifr(result, num))

#Задание 6
count = int(input("Введите количество чисел в списке: "))
nums = [int(input("Введите число: ")) for a in range(count)]
def lists(count:int, nums:list)->tuple:
    otr = list()
    not_otr = list()
    for i in nums:
        if i < 0:
            otr.append(i)
        else:
            not_otr.append(i)
    return sorted(otr, reverse=True), sorted(not_otr)

print(lists(3, nums))

#Задание 7
stroc = str(input("Введите строку: "))
new_stroc = ''.join(reversed(stroc))
len_stroc = len(stroc)/2

if len_stroc % 2 == 0:
    if stroc == new_stroc:
        print("Список является палиндромом")
    else:
        print("Список не является палиндромом")
else:
    if stroc == new_stroc:
        print("Список является палиндромом")
    else:
        print("Список не является палиндромом")

#Задание 8

def number():
    start = 1
    end = 100
    avg = (start + end) // 2
    step = 0
    while True:
         a = str(input(f"Твое число равно, меньше или больше {avg}: ")).lower()
         step += 1
         if a == "равно":
             print(f"Число {avg}, кол-во попыток {step}")
             break
         elif a == "больше":
             start = avg + 1
             avg = (start + end) // 2
         elif a == "меньше":
             end = avg - 1
             avg = (start + end) // 2
         else:
             print("Неверная команда")
             step -= 1

#Задание 9

def convert_to10(num, sistem):
    a = 0
    alfabeth = "0123456789ABCDEF"
    alf = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    for i in range(len(num)):
        n = alf[alfabeth.index(num[i])]
        a += n * (sistem**(len(num)-i-1))
    return a

print(convert_to10("45AB", 16))

def convert_to2(num, sistem):
    a = ""
    alfabeth = "0123456789ABCDEF"
    alf = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    while True:
        a += str(num % 2)
        num = num // 2
        if num == 0:
            break
        # n = alf[alfabeth.index(num[i])]
        # a += n * (sistem**(len(num)-i-1))
    return "".join(reversed(a))

print(convert_to2(convert_to10("45AB", 16), 10))

#Задание 10
import datetime

def magic_date(a:datetime.date)->bool:
    year = int(str(a.year)[2:])
    if a.month * a.day == year:
        return True

if __name__ == "__main__":
    day = datetime.date(year=1900, month=1, day=1)
    last_day = datetime.date(year=1999, month=12, day=31)
    while day <= last_day:
        if magic_date(day):
            print(f"Магическая дата {day}")
        day += datetime.timedelta(days=1)
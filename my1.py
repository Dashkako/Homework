import math
print()
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
del a [0]
del b [0]
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




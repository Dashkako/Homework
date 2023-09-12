
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

exams = sorted(info["ЕГЭ"])
print("Предметы:", exams)
uni = sorted(info["вузы"].keys())
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




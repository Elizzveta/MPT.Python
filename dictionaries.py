# 1. Создайте словарь из трёх учеников и их оценок. Выведите оценку одного ученика по его имени.

dict_1 = { 
    "Polina":5,
    "Dmitry":4,
    "Sergey":3
}

print(f"Оценка Polina составляет {dict_1['Polina']}")
print(f"Оценка Dmitry составляет {dict_1['Dmitry']}")
print(f"Оценка Sergey составляет {dict_1['Sergey']}")

# 2. Дан словарь. Добавьте в него новую пару, измените значение одного из ключей, удалите другой ключ и выведите результат.

dict_2 = {
    "surname": "Архипова",
    "name": "Наталья",
    "middle_name": "Сергеевна",
    "city":"Москва"
}
print(f"Первоначальный словарь: {dict_2}")

dict_2["name"] = "Ксения"
dict_2["age"] = 33 
del dict_2["city"] 

print(f"Измененный словарь: {dict_2}")

# 3. Дан словарь и ключ. Выведите значение по этому ключу, а если такого ключа нет, выведите «Нет такого ключа».

dict_3 = {
    "name":"Elizabeth",
    "login":"liza_veta",
    "password":"12598746^^mn"
}

key = input("Введите ключ: ")

if key in dict_3:
    print(f"Значение: {dict_3[key]}")
else:
    print("Нет такого ключа")

# 4. Дан словарь. Выведите отдельно все его ключи, все значения и количество пар.

dict_4 = {
    "surname": "Маркова",
    "name": "Алёна",
    "middle_name": "Викторовна",
    "city":"Одинцово",
    "age":18
}

print(f"Все ключи: {dict_4.keys()}")
print(f"Все значения: {dict_4.values()}")
print(f"Количество пар: {len(dict_4)}")

# 5. Дан словарь товаров и их цен. Выведите каждый товар и его цену с новой строки.

dict_5 = {
    "banana":129,
    "apple":30,
    "cherry":200,
    "blueberry":350,
    "strawberry":300
}
for key in dict_5:
    print(f"{key}:{dict_5[key]}")

# 6. Дан словарь товаров и их цен. Найдите сумму всех цен и название самого дорогого товара.

dict_6 = {
    "banana":129,
    "apple":30,
    "cherry":200,
    "blueberry":350,
    "strawberry":300
}

total = 0
max_price = 0
max_product = ""

for product in dict_6.keys():
    price = dict_5[product]
    total += price
    if price>max_price:
        max_price = price
        max_product = product

print(f"Сумма всех цен: {total}")
print(f"Название самого дорогого товара: {max_product}")

# 7. Дана строка. Посчитайте, сколько раз в ней встречается каждый символ, и сохраните результат в словарь.

text = input("Введите строку: ")
dict_7 = {}

for char in text:
    if char in dict_7:
        dict_7[char] += 1
    else:
        dict_7[char] = 1

print("Частоты символов:")
for char in dict_7:
    print(f"'{char}': {dict_7[char]}")

# 8. Дана строка из слов через пробел. Посчитайте, сколько раз встречается каждое слово, и выведите самое частое.

text = "кот собака кот птица кот собака рыба"

words = text.split()

dict_8 = {}
for word in words:
    if word in dict_8:
        dict_8[word] += 1
    else:
        dict_8[word] = 1

print("Частота слов:")
for word in dict_8:
    print(f"{word}: {dict_8[word]}")

max_count = 0
most_common = ""
for word in dict_8:
    if dict_8[word] > max_count:
        max_count = dict_8[word]
        most_common = word

print(f"Самое частое слово: {most_common} ({max_count} раз)")

# 9. Дан словарь. Создайте новый словарь, в котором ключи и значения поменяны местами.

dict_9 = {
    "banana": 129,
    "apple": 30,
    "cherry": 200,
    "blueberry": 350,
    "strawberry": 300
}

inverted = {}
for key in dict_9:
    inverted[dict_9[key]] = key

print("Исходный словарь:")
for key in dict_9:
    print(f"{key}: {dict_9[key]}")

print("Инвертированный словарь:")
for key in inverted:
    print(f"{key}: {inverted[key]}")

# 10. Даны два списка одинаковой длины: страны и их столицы. Составьте из них словарь и выведите столицу страны, которую введёт пользователь.

countries = ["Россия", "Франция", "Германия", "Италия", "Испания"]
capitals  = ["Москва", "Париж", "Берлин", "Рим", "Мадрид"]

dict_10 = {}
for i in range(len(countries)):
    dict_10[countries[i]] = capitals[i]

print("Словарь стран и столиц:")
for country in dict_10:
    print(f"{country}: {dict_10[country]}")

user_country = input("Введите страну: ")

if user_country in dict_10:
    print(f"Столица страны {user_country} — {dict_10[user_country]}")
else:
    print(f"Страна '{user_country}' не найдена в словаре")
# 1. Выведите все числа от 1 до 10 с помощью while.

num_1 = 1
while num_1<11:
    print(num_1)
    num_1+=1

# 2. Вводите числа, пока не будет введён 0. Выведите сумму введённых чисел.

num_2 = int(input("Введите число: "))
sum = 0
while num_2 != 0:
    sum+=num_2
    num_2 = int(input("Введите число: "))
print(f"Сумма введенных чисел: {sum}")

# 3. Дано натуральное число. Посчитайте количество его цифр.

num_3 = int(input("Введите число: "))
count = 0

while num_3>0:
    num_3 = num_3 // 10
    count+=1
print(f"Количество цифр в числе: {count}")

# 4. Дано натуральное число. Найдите сумму его цифр.

num_4 = int(input("Введите число: "))
summ = 0

while num_4>0:
    n = num_4 % 10
    summ+=n
    num_4 = num_4 // 10
print(f"Сумма чисел: {summ}")

# 5. Дано натуральное число. Выведите его цифры в обратном порядке одним числом.

num_5 = int(input("Введите число: "))
r_num = 0

while num_5>0:
    n = num_5 % 10
    r_num = r_num*10+n
    num_5 = num_5//10
print(r_num)


# 6. Дано число n. Выведите все степени двойки, не превышающие n.

n = int(input("Введите число: "))
degree = 1

while 2**degree<n:
    print(f"2 ** {degree} = {2**degree}")
    degree+=1


# 7. Запрашивайте пароль, пока пользователь не введёт правильный.

password = input("Установите пароль: ")
print("Вы вошли в  систему")


while True:
    attempt = input("Введите пароль: ")
    if attempt == password:
        print("Пароль верный")
        break
    else:
        print("Пароль неверный. Попробуйте снова")


# 8. Даны два натуральных числа. Найдите их наибольший общий делитель.

x = int(input("Введите число: "))
y = int(input("Введите число: "))

while y != 0 :
    x, y = y, x%y
print(f"Наибольший общий делитель равен: {x}")

# 9. Дано число n. Выведите все числа Фибоначчи, не превышающие n.

n = int(input("Введите число: "))
fib = 0
next_fib = 1

while fib<=n:
    print(fib)
    fib, next_fib = next_fib, fib + next_fib

# 10. Программа загадывает число от 1 до 100. Пользователь угадывает его, а программа отвечает «больше» или «меньше». В конце выведите количество попыток.

import random

number = random.randint(1,100)
count = 0

attempt = int(input("Введите ваше предположение: "))

while attempt!=number:
    count+=1
    if attempt<number:
        print("Загаданное число больше")
            
    else:
        print("Загаданное число меньше")
            
    attempt = int(input("Введите ваше предположение снова: "))
count+=1
print(f"Вы угадали, количество попыток: {count}")
            
# 1. Выведите все числа от 1 до 10.

for i in range(1,11):
    print(i)

# 2. Выведите все чётные числа от 2 до 50.

for i in range(2,51,2):
    print(i)

# 3. Выведите числа от 10 до 1 в порядке убывания.

for i in range(10,0,-1):
    print(i)

# 4. Дано число n. Найдите сумму всех чисел от 1 до n.

n = int(input("Введите число: "))
sum = 0

for i in range(1,n+1):
    sum+=i
print(sum)

# 5. Дано число n. Найдите его факториал.

n = int(input("Введите число: "))
fact = 1

for i in range(1,n+1):
    fact*=i
print(fact)

# 6. Дано число n. Выведите таблицу умножения на n от 1 до 10.

n = int(input("Введите число: "))

for i in range(1,11):
    print(f"{n} * {i} = {n*i}")

# 7. Дан список чисел. Посчитайте, сколько в нём положительных чисел.

lst = [-5,-4,-3,-2,-1,0,1,2,3,4,5]
count = 0

for num in lst:
    if num >0:
        count+=1

print(f"Положительных чисел: {count}")


# 8. Дана строка. Посчитайте, сколько в ней гласных букв.

strin = input("Введите стоку: ")
vowels = "аоуыэеёиюяqaeyuio"
count = 0

strin = strin.lower()

for char in strin:
    if char in vowels:
        count+=1
print(f"Количество гласных: {count}")

# 9. Дан список чисел. Найдите наибольший элемент, не используя max().

numbers = [1,22,13,37,8,20,14,31,44,41,14,1,34,47,35]
mx = 0

for i in numbers:
    if mx > i:
        continue
    else:
        mx = i
print(f"Максимальное значение: {mx}")

# 10. Выведите таблицу умножения от 1 до 9 в виде квадрата.

for i in range(1,10):
    for j in range(1,10):
        print(f"{i*j:2}",end = " ")
    print()
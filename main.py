import random

x = [random.randint(-50, 50) for i in range(25)]
print(x)
print("Минимальное значение: ", min(x))
print("Максимальное значение: ", max(x))

count_pos = 0
count_neg = 0
count_zero = 0

for i in x:
    if i > 0:
        count_pos += 1
        procent1 = count_pos / 25 * 100
    if i < 0:
        count_neg += 1
        procent2 = count_neg / 25 * 100
    if i % 10 == 0:
        count_zero += 1
        procent3 = count_zero / 25 * 100

print(f"Кол-во положительных чисел: {count_pos}, их процент от общего количества: {procent1}")
print(f"Кол-во отрицательных чисел: {count_neg}, их процент от общего количества: {procent2}")
print(f"Кол-во нулевых чисел: {count_zero}, их процент от общего количества: {procent3}")

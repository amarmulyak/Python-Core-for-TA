# Знайти всі чотирьохзначні числа, сума цифер яких дорівнює заданому числу
# Задане число. перевірити чи дане число є простим
# Задано ціле число N, вивести перші N чисел Фібоначчі
# Знайти сумі кубів цифер аданого натурального числа
# Заданий текст, вивести всі слова, які починаються на певну послідовніть символів
# З точністю до   обчислити наближене значення    для значень аргумента   та порівняти з точним значенням. Результати оформити у таблиці:

import numpy as np

a = 0.1
b = 0.8
h = 0.01
k = 1
p = 0
si = 1
s = 0
print("-" * 65)
print("|", "x".center(12), "\t|", "s".center(12), "\t|", "y".center(12), "\t|", "p".center(12), "\t|")
for x in np.arange(a, b, h):
    while si > 10 ** (-5):
        si = k * (k + 1) * (x ** k)
        s += si
        k += 1
    y = (2 * x) / ((1 - x) ** 3)
    p = np.abs((s - y) / y)
    print("|", f"{x:9.2f}", "\t|", f"{s:9.10f}", "\t|", f"{y:9.8f}", "\t|", f"{p:9.10f}", "\t|")
print("-" * 65)

a = 1
b = 2
h = 0.1
k = 0
p = 0
si = 1
s = 0
print("-" * 65)
print("|", "x".center(12), "\t|", "s".center(12), "\t|", "y".center(12), "\t|", "p".center(12), "\t|")
for x in np.arange(a, b, h):
    while si > 10 ** (-5):
        si = (1 / (np.math.factorial(k) * (k + 2))) * (x ** k)
        s += si
        k += 1
    y = (x - 1) * np.exp(x) + 1
    p = np.abs((s - y) / y)
    print("|", f"{x:9.1f}", "\t|", f"{s:9.10f}", "\t|", f"{y:9.10f}", "\t|", f"{p:9.10f}", "\t|")
print("-" * 65)

a = 0.1
b = 0.8
h = 0.1
n = 1
p = 0
si = 1
s = 0
print("-" * 65)
print("|", "x".center(12), "\t|", "s".center(12), "\t|", "y".center(12), "\t|", "p".center(12), "\t|")
for x in np.arange(a, b, h):
    while si > 10 ** (-5):
        si = n * (n + 2) * (x ** n)
        s += si
        n += 1
    y = (x * (3 - x)) / ((1 - x) ** 3)
    p = np.abs((s - y) / y)
    print("|", f"{x:9.1f}", "\t|", f"{s:9.10f}", "\t|", f"{y:9.8f}", "\t|", f"{p:9.10f}", "\t|")
print("-" * 65)

a = 0.1
b = 0.55
h = 0.05
n = 0
p = 0
si = 1
s = 0
print("-" * 65)
print("|", "x".center(12), "\t|", "s".center(12), "\t|", "y".center(12), "\t|", "p".center(12), "\t|")
for x in np.arange(a, b, h):
    while si > 10 ** (-5):
        si = (3 + 2 * n) * (x ** (n + 1))
        s += si
        n += 1
    y = (1 + x) / ((1 - x) ** 2)
    p = np.abs((s - y) / y)
    print("|", f"{x:9.2f}", "\t|", f"{s:9.10f}", "\t|", f"{y:9.8f}", "\t|", f"{p:9.10f}", "\t|")

print("-" * 65)


# Генерується квадратна матриця. Знайти сума елементів її головнї та побічної діагоналей.
# Головна діагональ йде з верхнього лівого кута в правий нижній, побічна - з верхнього правого кута в лівий нижній.
from random import random
N = 5
matrix = []
for i in range(N):
    row = []
    for j in range(N):
        row.append(int(random()*10))
    matrix.append(row)

for row in matrix:
    print(row)

sum_1 = 0
sum_2 = 0
for i in range(N):
    sum_1 += matrix[i][i]
    sum_2 += matrix[i][N-i-1]

print(sum_1)
print(sum_2)


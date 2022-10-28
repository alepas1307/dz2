# Задайте список из n чисел последовательности (1+1/n)n и выведите на экран их сумму

n = int(input('Введите число: '))
numbers = {}
a = 0
sum = 0

for i in range(1,n+1):
    a = (1+1/i)**i
    numbers[i] = round(a,2)
    sum +=a

print(f'Последовательность: {numbers}')
print(f'Сумма чисел последовательности = {round(sum,2)}')
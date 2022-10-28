# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

number = abs(int(input('Введите целое число: ')))
mult = 1
list = []
for i in range(1,number+1):
    mult *=i
    list.append(mult)
print(list)
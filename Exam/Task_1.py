#-----------------ЗАДАЧА №1-----------------------#

'''Четное или нечетное число: Напишите программу, 
# которая проверяет, является ли введенное 
# пользователем число четным или нечетным.'''

num_input = int(input('Введите число: '))

if num_input%2 == 0:
    print('Вы ввели чётное число')
else: 
    print('Вы ввели не чётное число')    
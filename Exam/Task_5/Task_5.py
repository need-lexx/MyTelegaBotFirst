#-------------------ЗАДАЧА №5-----------------------#

'''Запись текста в файл: Напишите программу, которая
запрашивает у пользователя строку текста и записывает ее в
файл.'''


def write_file(f_name, text):
    with open(f_name, 'a', encoding='utf-8') as file:               
        file.write(text) 

file_name = 'Задание 5.txt' 

input_text = input('Введите текст для записи: ')

text = input_text + '\n'

write_file(file_name, text)

# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

import os

path = os.path.abspath("text1.txt") # определяем адрес файла

def readFile(str):
    data = open(str, "r")
    line = data.readline()
    data.close()
    return line

my_string = readFile(path)
print(f" Превоначальная строка: {my_string}")
arhive_str = ""
while len(my_string) > 0:
    i = 1
    while my_string[i] == my_string[i - 1]:
        i += 1
        if i >= len(my_string):
            break
    arhive_str += str(i) + my_string[i - 1]
    my_string = my_string[i:]
print(f"Архивированная строка: {arhive_str}")

unpack_str = ""
temp1_list = list(i for i in arhive_str if i.isdigit()) # список из цифр
temp2_list = list(i for i in arhive_str if not i.isdigit()) # список из букв

for i in range(len(temp2_list)):
    unpack_str += int(temp1_list[i]) * temp2_list[i]
print(f"Распакованная строка: {unpack_str}")

def write_file(str, file):   # функция для записи строки в файл
    path = os.path.abspath(file)
    with open(path, "w") as data:
        data.write(str)

write_file(arhive_str, "text2.txt")
write_file(unpack_str, "text3.txt")

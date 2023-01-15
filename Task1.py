# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

str = "ыдвао длаод одпло плофыэабвжвафыэва ж жп жывп жыпж жфывабвпэжы вопфыжвпж пж ып"
print(str)
str_is_in = "абв"
str = str.split()

temp_str = ""
for i in filter(lambda str: not str_is_in in str, str):
    temp_str += " " + i
str = temp_str[1:]
print(str)
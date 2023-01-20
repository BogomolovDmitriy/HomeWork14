# Игра 13 спичек. можно брать до 3-х спичек за один ход. Кому досталась последняя спичка - тот проиграл.
# Первый ход определяется случайным образом.
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

# ////////////////////////////
# игра на двоих
# ////////////////////////////

from random import randint

# name1 = input("Введите имя первого игрока: ")
# name2 = input("Введите имя второго игрока: ")

# choosing_move = randint(0, 1)
# if choosing_move == 0:
#     step = 1
#     print("Игру начинает " + name1)
# else:
#     step = 2
#     print("Игру начинает " + name2)

# def take_input(name, match):
#     while True:
#         count = input(name + ", сколько взять спичек " + " ? ")
#         if not (count in "123"):
#             print("Ошибочный ввод. Повторите.")
#             continue
#         count = int(count)
#         if (match - count) < 1:
#             print(name + "Столько спичек нет в остатке, возьмите меньшее количество!")
#             continue
#         match -= count
#         break
#     if match in list(i for i in range(2, 5)):
    #     print(f"Осталось {match} спички.")
    # elif match == 1:
    #     print(f"Осталось {match} спичка.")
    # else:
    #     print(f"Осталось {match} спичек.")
#     return match
        
# def chek_win(match, step):
#     if match == 1:
#         if step == 2:
#             return name1
#         else:
#             return name2
#     return False

# def game(step):
#     match = 13
#     while True:
#         if step == 1:
#             match = take_input(name1, match)
#             step = 2
#         elif step == 2:
#             match = take_input(name2, match)
#             step = 1
#         winner = chek_win(match, step)
#         if winner:
#             print(winner + ", Вы выиграли!")
#             break

# game(step)


# //////////////////////////////////////////////////////
# игра с ботом
# //////////////////////////////////////////////////////

# name1 = input("Введите имя игрока: ")
# name2 = "bot"

# choosing_move = randint(0, 1)
# if choosing_move == 0:
#     step = 1
#     print("Игру начинает " + name1)
# else:
#     step = 2
#     print("Игру начинает " + name2)

# def take_input(name, match):
#     while True:
#         if name == "bot":
#             count = randint(1, 3)
#             if count == 1:
#                 print(f"{name} взял {count} спичку.")
#             else:
#                 print(f"{name} взял {count} спички.")
#         else:
#             count = input(name + ", сколько взять спичек " + " ? ")
#             if not (count in "123"):
#                 print("Ошибочный ввод. Повторите.")
#                 continue
#             count = int(count)
#             if (match - count) < 1:
#                 print(name + ", столько спичек нет в остатке, возьмите меньшее количество!")
#                 continue
#         match -= count
#         break
#     if match in list(i for i in range(2, 5)):
#         print(f"Осталось: {match} спички.")
#     elif match == 1:
#         print(f"Осталось: {match} спичка.")
#     else:
#         print(f"Осталось: {match} спичек.")

#     return match
        
# def chek_win(match, step):
#     if match == 1:
#         if step == 2:
#             return name1
#         else:
#             return name2
#     return False

# def game(step):
#     match = 13
#     while True:
#         if step == 1:
#             match = take_input(name1, match)
#             step = 2
#         elif step == 2:
#             match = take_input(name2, match)
#             step = 1
#         winner = chek_win(match, step)
#         if winner:
#             print(winner + ", Вы выиграли!")
#             break

# game(step)



# //////////////////////////////////////////////////////
# игра с умным ботом
# //////////////////////////////////////////////////////


name1 = input("Введите имя игрока: ")
name2 = "bot"

choosing_move = randint(0, 1)
if choosing_move == 0:
    step = 1
    print("Игру начинает " + name1)
else:
    step = 2
    print("Игру начинает " + name2)

def take_input(name, match):
    while True:
        if name == "bot":
            if match < 5:
                for i in range(1, 4):
                    if (match - i) == 1:
                        count = i
            else:
                for i in range(1, 4):                
                    if (match - i - 1) % 4 == 0:
                        count = i
                    else:
                        count = 1
                if count == 1:
                    print(f"{name} взял {count} спичку.")
                else:
                    print(f"{name} взял {count} спички.")                
        else:
            count = input(name + ", сколько взять спичек " + " ? ")
            if not (count in "123"):
                print("Ошибочный ввод. Повторите.")
                continue
            count = int(count)
            if (match - count) < 1:
                print(name + ", столько спичек нет в остатке, возьмите меньшее количество!")
                continue
        match -= count
        break
    if match in list(i for i in range(2, 5)):
        print(f"Осталось: {match} спички.")
    elif match == 1:
        print(f"Осталось: {match} спичка.")
    else:
        print(f"Осталось: {match} спичек.")

    return match
        
def chek_win(match, step):
    if match == 1:
        if step == 2:
            return name1
        else:
            return name2
    return False

def game(step):
    match = 13
    while True:
        if step == 1:
            match = take_input(name1, match)
            step = 2
        elif step == 2:
            match = take_input(name2, match)
            step = 1
        winner = chek_win(match, step)
        if winner:
            print(winner + ", Вы выиграли!")
            break

game(step)
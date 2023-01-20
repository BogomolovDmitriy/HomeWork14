# Создайте программу для игры в ""Крестики-нолики"".

board = [i for i in range(1, 10)]

victoris = [(1, 2, 3), (4, 5, 6,), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)]

name1 = input("Введите имя первого игрока: ")
while True:
    player1_simbol = input("Введите свой символ (Х или О на латинской раскладке): ").upper()
    if not (player1_simbol in "XO"):
        print("Ошибочный ввод. Повторите.")
        continue
    else:
        break
    
name2 = input("Введите имя второго игрока: ")
while True:
    player2_simbol = input("Введите свой символ (Х или О на латинской раскладке): ").upper()
    if not (player2_simbol in "XO") or player2_simbol == player1_simbol:
        print("Ошибочный ввод. Повторите.")
        continue
    else:
        break
    
def printBoard():
    print(".............")
    for i in range(3):
        print(f"| {board[0 + i * 3]} | {board[1 + i * 3]} | {board[2 + i * 3]} |")
    print(".............")

def take_input(name, player_simbol):
    while True:
        value = input(name + ", Куда ставить " + '"' + player_simbol + '"' + " ? ")
        if not (value in "123456789"):
            print("Ошибочный ввод. Повторите.")
            continue
        value = int(value)
        if str(board[value - 1]) in "XO":
            print("Позиция занята. Выбирите другую позицию.")
            continue
        board[value - 1] = player_simbol
        break

def chek_win():
    for i in victoris:
        if (board[i[0] - 1]) == (board[i[1] - 1]) == (board[i[2] - 1]):
            if board[i[1] - 1] == player1_simbol:
                return name1
            else:
                return name2
    return False

def game():
    count = 0
    while True:
        printBoard()
        if count % 2 == 0:
            take_input(name1, player1_simbol)
        else:
            take_input(name2, player2_simbol)
        if count > 3:
            winner = chek_win()
            if winner:
                printBoard()
                print(winner, "выиграл!")
                break
        count += 1
        if count > 8:
            printBoard()
            print("ничья!")
            break
game()




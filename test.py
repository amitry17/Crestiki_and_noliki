
# Создаю игровоу поле "матрицу" для игры
L = []

for i in range(4):
    for j in range(4):
        if i == 0:
            L.append(j)
        elif j == 0:
            L.append(i)
        else: L.append("-")

play_ground = [L[i:i+4] for i in range(0, len(L), 4)]



""" for i in range(4):
    print(*play_ground[i]) """

# функция по индексу вставляет символ введенный игроком

def player_step(i,j,symbol):
    global play_ground
    play_ground[i][j] = symbol

# Плохой код для выявления победителя
def who_win(play_ground):
    win = ""
    for i in range(1,4):
        if play_ground[i][1] == "O" and play_ground[i][2] == "O" and play_ground[i][3] == "O":
                win = "O"
        elif play_ground[i][1] == "X" and play_ground[i][2] == "X" and play_ground[i][3] == "X":
                win = "X"
        elif play_ground[1][i] == "O" and play_ground[2][i] == "O" and play_ground[3][i] == "O":
                win = "O"
        elif play_ground[1][i] == "X" and play_ground[2][i] == "X" and play_ground[3][i] == "X":
                win = "X"
        elif play_ground[1][i] == "X" and play_ground[2][i] == "X" and play_ground[3][i] == "X":
                win = "X"
    if play_ground[1][1] == "X" and play_ground[2][2] == "X" and play_ground[3][3] == "X":
          win = "X"
    elif play_ground[1][1] == "O" and play_ground[2][2] == "O" and play_ground[3][3] == "o":
          win = "O"
    elif play_ground[3][1] == "X" and play_ground[2][2] == "X" and play_ground[1][3] == "X":
          win = "X"
    elif play_ground[3][1] == "O" and play_ground[2][2] == "O" and play_ground[1][3] == "O":
          win = "O"
    return win
        
        
# Цикл игры 
game_over = False
first_player = True
while game_over == False:
      for i in range(4):
            print(*play_ground[i])
      if first_player == True:
            symbol = "O"
            print("Игрок O")
            i = int(input("Введите значение y:"))
            j = int(input("Введите значение x:"))
      else: 
            symbol = "X"
            print("Игрок X")
            i = int(input("Введите значение y:"))
            j = int(input("Введите значение x:"))  
      player_step(i,j,symbol)
      
      win = who_win(play_ground) 
      if win != "":
        game_over = True
      else:
        game_over = False

      first_player = not first_player

for i in range(4):
    print(*play_ground[i]) 

print("Победил", win)

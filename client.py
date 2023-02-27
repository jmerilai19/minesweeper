import minesweeper

def print_board(matrix):
    for y in range(len(matrix)):
        for x in range(len(matrix[y])):
            print(matrix[y][x], end=" ")
        print()

def minesweeper_console():
    game = minesweeper.Game(5)
    print_board(game.start()[1])

    print("Open or flag a field by typing x y or flag xy. Example: 1 1 or flag 1 1")

    while True:
        command = input().split(" ")
        
        if len(command) == 2:
            try:
                x, y = int(command[0]), int(command[1])
            except Exception as e:
                print("Invalid input")
            else:
                status, board = game.play(x, y, "open")
                if status == 0:
                    print_board(board)
                elif status == 1:
                    print_board(board)
                    print("You win")
                    exit()
                elif status == 2:
                    print_board(board)
                    print("You lose")
                    exit()
                elif status == -1:
                    print("Invalid input")
        elif len(command) == 3:
            if not command[0] == "flag":
                print("Invalid input0")
            else:
                try:
                    x, y = int(command[1]), int(command[2])
                except Exception as e:
                    print("Invalid input1")
                else:
                    status, board = game.play(x, y, "flag")
                    if status == 0:
                        print_board(board)
                    elif status == -1:
                        print("Invalid input2")

if __name__ == "__main__":
    minesweeper_console()
    
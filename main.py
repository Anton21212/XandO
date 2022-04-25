board = [i for i in range(1, 10)]


def print_board(board):
    print("-" * 13)
    for i in range(3):
        print("|", board[0 + i * 3], "|", board[1 + i * 3], "|", board[2 + i * 3], "|")
        print("-" * 13)


def move(who, player):
    while True:
        figure = int(input(f" {player}, введите поле в диапазоне от 1 до 9 включительно "))
        if figure <= 9:
            if str(board[figure - 1]) not in "XY":
                board[figure - 1] = who
                break
        else:
            print("Повторите попытку")


def find_winner(board):
    winser = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    for i in winser:
        if (board[i[0]]) == (board[i[1]]) == (board[i[2]]):
            return board[i[0]]


def main():
    amount = 0
    while True:
        print_board(board)
        if amount % 2 == 0:
            move("X", "Ходи X")
        else:
            move("Y", "Ходи Y")
        if amount > 3:
            gamer = find_winner(board)
            if gamer:
                print(gamer, "win")
                break
        amount += 1
        if amount == 9:
            print("Ничья")
    print_board(board)


main()


class XO:
    def __init__(self):
        self.board = [i for i in range(1, 10)]

    def print_board(self):
        print("-" * 13)
        for i in range(3):
            print("|", self.board[0 + i * 3], "|", self.board[1 + i * 3], "|", self.board[2 + i * 3], "|")
            print("-" * 13)

    def move(self, who, player):
        while True:
            try:
                figure = int(input(f"{player}, введите поле в диапазоне от 1 до 9 включительно "))
            except ValueError:
                print("Введите число")
                continue
            if figure <= 9:
                if str(self.board[figure - 1]) not in "XY":
                    self.board[figure - 1] = who
                    break
                else:
                    print("Позиция занята")
            else:
                print("Повторите попытку")

    def find_winner(self):
        winning_combination = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
        for i in winning_combination:
            if (self.board[i[0]]) == (self.board[i[1]]) == (self.board[i[2]]):
                return self.board[i[0]]

    def run(self):
        amount = 0
        while True:
            self.print_board()
            if amount % 2 == 0:
                self.move("X", "Ходит X")
            else:
                self.move("Y", "Ходит Y")
            if amount > 3:
                gamer = self.find_winner()
                if gamer:
                    print(gamer, "win")
                    break
            amount += 1
            if amount == 9:
                print("Ничья")
        self.print_board()


if __name__ == '__main__':
    XO().run()

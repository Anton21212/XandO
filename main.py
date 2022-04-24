board = [i for i in range(1, 10)]
def my_board(board):
    print("-" * 13)
    for i in range(3):
        print("|", board[0 + i * 3], "|", board[1 + i * 3], "|", board[2 + i * 3], "|")
        print("-" * 13)


def player(who):
    Q = 0
    while Q != 1:
        X = int(input("Введите поле в диапазоне от 1 до 9 включительно "))
        if str(board[X - 1]) not in "XY":
            board[X - 1] = who
            my_board(board)
            Q = 1


def winner(board):
    winser = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    for i in winser:
        if (board[i[0]]) == (board[i[1]]) == (board[i[2]]):
            return board[i[0]]
    return False

def main():
    amount = 0
    win = False
    while not win:
        my_board(board)
        if amount % 2 == 0:
            player("X")
        else:
            player("Y")
        if amount > 3:
            gamer = winner(board)
            if gamer:
                print(gamer, "win")
                break
        amount += 1
        if amount == 9:
            print("Ничья")
    my_board(board)


main()



# class Tree():
#     def __init__(self,a):
#         self.a = a
#         self.age = 0
#         self.height = 0
#     def info(self):
#         return f"{self.a}, {self.age}, {self.height}"
#
#     def plus(self):
#         self.age +=10
#         self.height+=1
# #
# #
# # class Fruit_Tree(Tree):
# #     def amount_fruti(self):
# #         s = self.age//2
# #         return f"{s}"
#
#
# c = Fruit_Tree("Tree")
# c.plus()
# c.plus()
# c.info()
# c.amount_fruti()
# print(c.info())
# print(c.amount_fruti())

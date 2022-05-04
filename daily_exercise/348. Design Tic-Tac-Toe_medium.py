class TicTacToe:

    def __init__(self, n: int):
        self.dim = n
        self.board = [[0] * n] * n
        self.record_dict = defaultdict(list)
        self.end = False

    def move(self, row: int, col: int, player: int) -> int:

        if not self.end:
            self.record_dict[row].append(player)
            self.record_dict[self.dim + col].append(player)
            if row == col:
                self.record_dict[2 * self.dim].append(player)
            if row == self.dim - col - 1:
                self.record_dict[2 * self.dim + 1].append(player)

            for i in [row, self.dim + col, 2 * self.dim, 2 * self.dim + 1]:
                if len(self.record_dict[i]) == self.dim and self.check_win(self.record_dict[i]):
                    return player

            return 0

    def check_win(self, candidate):
        if 1 not in candidate or 2 not in candidate:
            self.end = True
            return True
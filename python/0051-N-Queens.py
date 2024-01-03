class Solution:
    def backtrack(self, row):
        if row == self.n:
            solution = ["".join(board_row) for board_row in self.board]
            self.res.append(solution)
            return

        # check all cols
        for col in range(self.n):
            pos_diagonal_value = row + col
            neg_diagonal_value = row - col
            if (
                # if is in this col
                col in self.occupied_cols
                # if is in pos diagonal+
                or pos_diagonal_value in self.occupied_pos_diagonals
                # if is in neg diagonal-
                or neg_diagonal_value in self.occupied_neg_diagonals

            ):
                # this place can't be used
                continue

            # mark as used
            self.occupied_cols.add(col)
            self.occupied_pos_diagonals.add(pos_diagonal_value)
            self.occupied_neg_diagonals.add(neg_diagonal_value)

            # check if this solution fits
            self.board[row][col] = "Q"
            self.backtrack(row + 1)
            self.board[row][col] = "."

            # unmark as used
            self.occupied_cols.remove(col)
            self.occupied_pos_diagonals.remove(pos_diagonal_value)
            self.occupied_neg_diagonals.remove(neg_diagonal_value)

    def solveNQueens(self, n: int) -> List[List[str]]:
        self.n = n
        # col
        self.occupied_cols = set()
        # row + col
        self.occupied_pos_diagonals = set()
        # row - col
        self.occupied_neg_diagonals = set()

        self.res = []
        self.board = [["."] * n for _ in range(n)]
        self.backtrack(0)

        return self.res

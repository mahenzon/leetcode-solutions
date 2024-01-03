class Solution:
    def backtrack(self, row: int) -> None:
        if row == self.n:
            self.res += 1
            return

        for col in range(self.n):
            pos_diagonal = row + col
            neg_diagonal = row - col
            # check place can be used
            if (
                # col is occupied
                col in self.occupied_cols
                # pos diagonal is occupied
                or pos_diagonal in self.occupied_pos_diagonal
                # neg diagonal is occupied
                or neg_diagonal in self.occupied_neg_diagonal
            ):
                continue

            # mark as occupied
            self.occupied_cols.add(col)
            self.occupied_pos_diagonal.add(pos_diagonal)
            self.occupied_neg_diagonal.add(neg_diagonal)

            # check this place
            self.board[row][col] = "Q"
            self.backtrack(row + 1)
            self.board[row][col] = "."

            # unmark as occupied
            self.occupied_cols.remove(col)
            self.occupied_pos_diagonal.remove(pos_diagonal)
            self.occupied_neg_diagonal.remove(neg_diagonal)

    def totalNQueens(self, n: int) -> int:
        self.n = n
        # col
        self.occupied_cols = set()
        # row + col
        self.occupied_pos_diagonal = set()
        # row - col
        self.occupied_neg_diagonal = set()

        self.board = [["."] * n for _ in range(n)]
        self.res = 0
        self.backtrack(0)
        return self.res

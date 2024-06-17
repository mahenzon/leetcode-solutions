class Solution:
    def backtrack(self, row: int) -> None:
        if row == self.n:
            self.res += 1
            return

        for col in range(self.n):
            pos_idx = row + col
            neg_idx = row - col

            if (
                col in self.occupied_cols
                or
                pos_idx in self.occupied_pos_diag
                or
                neg_idx in self.occupied_neg_diag
            ):
                # skip this combination
                continue

            # mark as occupied
            self.occupied_cols.add(col)
            self.occupied_pos_diag.add(pos_idx)
            self.occupied_neg_diag.add(neg_idx)

            # check next row
            self.board[row][col] = "Q"
            self.backtrack(row + 1)
            self.board[row][col] = "."

            # free space
            self.occupied_cols.remove(col)
            self.occupied_pos_diag.remove(pos_idx)
            self.occupied_neg_diag.remove(neg_idx)

    def totalNQueens(self, n: int) -> int:
        self.n = n
        # cols
        self.occupied_cols = set()
        # row + col
        self.occupied_pos_diag = set()
        # row - col
        self.occupied_neg_diag = set()

        self.board = [["."] * n for _ in range(n)]
        self.res = 0
        self.backtrack(0)
        return self.res

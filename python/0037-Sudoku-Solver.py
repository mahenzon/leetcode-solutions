class Solution:
    nums = "".join(map(str, range(1, 10)))

    def is_valid(self, row: int, col: int, val: str) -> bool:
        """
        Check this num is not present on the board
        in this row and this col and this 3x3 sub-box.
        """
        box_row = row // 3 * 3
        box_col = col // 3 * 3
        for i in range(9):
            if (
                # this 3x3 sector
                self.board[box_row + i // 3][box_col + i % 3] == val
                # check all cols in this row
                or self.board[row][i] == val
                # check all rows in this col
                or self.board[i][col] == val
            ):
                return False

        return True

    def solve(self, idx: int) -> bool:
        if idx == 81:
            # finish when already checked all cells
            return True

        row = idx // 9
        col = idx % 9

        if self.board[row][col] != ".":
            return self.solve(idx + 1)

        for num in self.nums:
            if not self.is_valid(row, col, num):
                continue
            self.board[row][col] = num
            if self.solve(idx + 1):
                return True
            self.board[row][col] = "."

        return False

    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.board = board
        self.solve(0)

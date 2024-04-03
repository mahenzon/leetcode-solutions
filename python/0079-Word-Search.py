class Solution:
    def dfs(self, row, col, idx):
        if idx == len(self.word):
            return True

        if (
            row < 0
            or
            col < 0
            or
            row >= self.rows
            or
            col >= self.cols
            or
            self.word[idx] != self.board[row][col]
            or
            (row, col) in self.paths
        ):
            return False

        self.paths.add((row, col))

        res = False
        for r, c in [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1),
        ]:
            if self.dfs(row + r, col + c, idx + 1):
                res = True
                break

        self.paths.remove((row, col))

        return res

    def exist(self, board: List[List[str]], word: str) -> bool:
        self.rows = len(board)
        self.cols = len(board[0])
        self.board = board
        self.word = word
        self.paths = set()

        for row in range(self.rows):
            for col in range(self.cols):
                if self.dfs(row, col, 0):
                    return True
        return False

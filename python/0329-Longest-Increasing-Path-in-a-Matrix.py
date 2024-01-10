class Solution:

    def dfs(self, row_idx: int, col_idx: int, last_val: int) -> int:
        if (
            row_idx < 0
            or row_idx == self.rows_count
            or col_idx < 0
            or col_idx == self.cols_count
        ):
            return 0

        val = self.matrix[row_idx][col_idx]
        if val <= last_val:
            return 0

        if self.cache[row_idx][col_idx] != -1:
            return self.cache[row_idx][col_idx]

        res = 1 + max(
            self.dfs(row_idx + 1, col_idx, val),
            self.dfs(row_idx - 1, col_idx, val),
            self.dfs(row_idx, col_idx + 1, val),
            self.dfs(row_idx, col_idx - 1, val),
        )
        self.cache[row_idx][col_idx] = res
        return res

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        self.matrix = matrix
        self.rows_count = len(matrix)
        self.cols_count = len(matrix[0])
        self.cache = [[-1] * self.cols_count for _ in range(self.rows_count)]
        return max(
            self.dfs(row_idx, col_idx, -1)
            for row_idx in range(self.rows_count)
            for col_idx in range(self.cols_count)
        )

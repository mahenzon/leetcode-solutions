class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        ROWS = len(grid)
        COLS = len(grid[0])

        ones_rows = [0] * ROWS
        ones_cols = [0] * COLS

        for row_i, row in enumerate(grid):
            for col_i, val in enumerate(row):
                if val:
                    ones_rows[row_i] += 1
                    ones_cols[col_i] += 1

        for row_i, row in enumerate(grid):
            for col_i, val in enumerate(row):
                grid[row_i][col_i] = (
                    2 * (
                        ones_rows[row_i]
                        + ones_cols[col_i]
                    ) - ROWS - COLS
                )

        return grid

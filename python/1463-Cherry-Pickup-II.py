class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        max_row_cherries = [[0] * COLS for _ in range(COLS)]
        for row in range(ROWS - 1, -1, -1):
            new_max_row_cherries = [[0] * (COLS + 1) for _ in range(COLS)]
            for col1 in range(COLS - 1):
                for col2 in range(col1 + 1, COLS):
                    max_cherries = 0
                    this_combination_cherries = grid[row][col1] + grid[row][col2]
                    for shift_1 in (-1, 0, 1):
                        for shift_2 in (-1, 0, 1):
                            c1 = col1 + shift_1
                            c2 = col2 + shift_2
                            if not (
                                0 <= c1 < COLS
                                and
                                0 <= c2 < COLS
                            ):
                                continue

                            max_cherries = max(
                                max_cherries,
                                this_combination_cherries + max_row_cherries[c1][c2]
                            )
                    new_max_row_cherries[col1][col2] = max_cherries

            max_row_cherries = new_max_row_cherries

        return max_row_cherries[0][COLS - 1]

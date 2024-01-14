class Solution:

    def dfs(self, to_visit: int, row: int, col: int) -> int:
        elem = self.grid[row][col]
        if elem == 2:
            # it's the end, and we have exactly one step left to visit it:
            return to_visit == 1

        res = 0
        # mark this one as visited
        self.grid[row][col] = -2
        # check cells for all the neighbours
        for row_inc, col_inc in [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1),
        ]:
            new_row = row + row_inc
            new_col = col + col_inc
            if (
                # row in bounds
                0 <= new_row < self.rows
                # and new col is in bounds
                and 0 <= new_col < self.cols
                # and it can be visited
                and self.grid[new_row][new_col] >= 0
            ):
                res += self.dfs(to_visit - 1, new_row, new_col)
        # mark as empty (revert back)
        self.grid[row][col] = elem
        return res

    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])

        can_be_visited = 0
        start_row = -1
        start_col = -1

        for row_idx, row in enumerate(grid):
            for col_idx, value in enumerate(row):
                if value >= 0:
                    can_be_visited += 1

                    if value == 1:
                        start_row = row_idx
                        start_col = col_idx

        return self.dfs(can_be_visited, start_row, start_col)

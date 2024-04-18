class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0
        for row_idx, row in enumerate(grid):
            for col_idx, val in enumerate(row):
                if not val:
                    continue
                perimeter += 4
                if row_idx > 0 and grid[row_idx - 1][col_idx]:
                    perimeter -= 2
                if col_idx > 0 and row[col_idx - 1]:
                    perimeter -= 2

        return perimeter

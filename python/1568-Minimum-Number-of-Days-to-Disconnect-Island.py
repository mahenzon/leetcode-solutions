class Solution:
    shifts = (
        (1, 0),
        (0, 1),
        (-1, 0),
        (0, -1),
    )

    def flood_fill(self, row, col, visited):
        key = row, col
        if (
            row < 0
            or row >= len(self.grid)
            or col < 0
            or col >= len(self.grid[0])
            or key in visited
            or not self.grid[row][col]
        ):
            return
        visited.add(key)
        for r, c in self.shifts:
            self.flood_fill(row + r, col + c, visited)

    def count_islands(self) -> int:
        count = 0
        visited = set()
        for row, row_values in enumerate(self.grid):
            for col, value in enumerate(row_values):
                if value and (row, col) not in visited:
                    self.flood_fill(row, col, visited)
                    count += 1

        return count

    def minDays(self, grid: List[List[int]]) -> int:
        self.grid = grid

        count = self.count_islands()

        if count != 1:
            return 0

        for row, row_values in enumerate(grid):
            for col, value in enumerate(row_values):
                if not value:
                    continue
                grid[row][col] = 0
                count = self.count_islands()
                if count != 1:
                    return 1
                grid[row][col] = 1

        return 2

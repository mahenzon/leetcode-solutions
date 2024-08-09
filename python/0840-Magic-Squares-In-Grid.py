class Solution:
    # this is a constant pattern of magic sequence
    p1 = "43816729" * 2
    p2 = p1[::-1]

    nei = (
        (-1, 0),
        (-1, 1),
        (0, 1),
        (1, 1),
        (1, 0),
        (1, -1),
        (0, -1),
        (-1, -1),
    )

    def is_magic(self, row, col) -> bool:
        if self.grid[row][col] != 5:
            return False

        seq = "".join(
            f"{self.grid[row + r][col + c]}"
            for r, c in self.nei
        )
        return seq in self.p1 or seq in self.p2

    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        self.grid = grid
        return sum(
            self.is_magic(row, col)
            for row in range(1, len(grid) - 1)
            for col in range(1, len(grid[0]) - 1)
        )

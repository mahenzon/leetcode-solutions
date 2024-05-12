class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        ni = n - 2
        res = [[0] * ni for _ in range(ni)]
        for r in range(ni):
            for c in range(ni):
                for i in range(r, r + 3):
                    for j in range(c, c + 3):
                        res[r][c] = max(
                            res[r][c],
                            grid[i][j],
                        )
        return res

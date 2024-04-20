class Solution:
    def dfs(self, row_idx: int, col_idx: int, end_cell: List[int]) -> None:
        if row_idx < 0 or row_idx == len(self.land) or col_idx < 0 or col_idx == len(self.land[0]):
            return
        if self.land[row_idx][col_idx] != 1:
            return
        self.land[row_idx][col_idx] = -1
        end_cell[0] = max(end_cell[0], row_idx)
        end_cell[1] = max(end_cell[1], col_idx)
        self.dfs(row_idx + 1, col_idx, end_cell)
        self.dfs(row_idx, col_idx + 1, end_cell)

    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        self.land = land
        res = []
        for row_idx, row in enumerate(self.land):
            for col_idx, val in enumerate(row):
                if val == 1:
                    end_cell = [row_idx, col_idx]
                    self.dfs(row_idx, col_idx, end_cell)
                    res.append([row_idx, col_idx, *end_cell])
        return res

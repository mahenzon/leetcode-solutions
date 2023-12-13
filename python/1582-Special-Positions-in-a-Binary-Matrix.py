class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        count = 0
        rows = [0] * len(mat)
        cols = [0] * len(mat[0])
        for row_i, row in enumerate(mat):
            for col_i, val in enumerate(row):
                if val:
                    rows[row_i] += 1
                    cols[col_i] += 1

        for row_i, row in enumerate(mat):
            for col_i, val in enumerate(row):
                if val and rows[row_i] == 1 and cols[col_i] == 1:
                    count += 1

        return count

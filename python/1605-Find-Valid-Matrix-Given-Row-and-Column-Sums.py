class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        rows = len(rowSum)
        cols = len(colSum)

        result = [[0] * cols for _ in range(rows)]

        row = 0
        col = 0

        while row < rows and col < cols:
            new_val = min(rowSum[row], colSum[col])
            result[row][col] = new_val
            rowSum[row] -= new_val
            colSum[col] -= new_val

            if rowSum[row]:
                col += 1
            else:
                row += 1

        return result

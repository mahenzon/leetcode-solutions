class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        # matrix is N x N
        N = len(matrix)

        for row_idx in range(N - 1):
            row = matrix[row_idx]
            next_row_idx = row_idx + 1
            for col_idx, min_val in enumerate(row):
                if col_idx > 0 and (left_val := row[col_idx - 1]) < min_val:
                    min_val = left_val
                if col_idx + 1 < N and (right_val := row[col_idx + 1]) < min_val:
                    min_val = right_val
                matrix[next_row_idx][col_idx] += min_val

        return min(matrix[-1])

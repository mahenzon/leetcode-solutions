class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        return [
            [row[i] for row in matrix]
            for i in range(len(matrix[0]))
        ]

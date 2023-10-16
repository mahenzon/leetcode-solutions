class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]
        for row_len in range(1, rowIndex + 1):
            prev_row = row
            row = [1]
            for idx in range(1, row_len + 1):
                total = prev_row[idx - 1]
                if idx < row_len:
                    total += prev_row[idx]
                row.append(total)
        return row

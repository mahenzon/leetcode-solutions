from collections import defaultdict


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)  # idx_col
        rows = defaultdict(set)  # idx_row
        boxes = defaultdict(set)  # [idx_row, idx_col]

        for idx_row, row in enumerate(board):
            for idx_col, el in enumerate(row):
                if el == ".":
                    continue

                idx_box = (idx_row // 3, idx_col // 3)
                if (
                    el in cols[idx_col]
                    or el in rows[idx_row]
                    or el in boxes[idx_box]
                ):
                    return False

                cols[idx_col].add(el)
                rows[idx_row].add(el)
                boxes[idx_box].add(el)

        return True

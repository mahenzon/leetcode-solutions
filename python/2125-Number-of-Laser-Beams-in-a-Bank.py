class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        res = 0
        prev_count = 0
        for lasers_row in bank:
            count = lasers_row.count("1")
            res += count * prev_count
            if count:
                prev_count = count
        return res

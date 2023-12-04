class Solution:
    def largestGoodInteger(self, num: str) -> str:
        res = ""
        count = 0
        prev_n = ""
        for n in num:
            if n != prev_n:
                count = 0
            prev_n = n
            count += 1
            if (
                count == 3
                and (
                    (not res) or n > res
                )
            ):
                res = n

        return res * 3

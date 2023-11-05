class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        res = arr[0]
        count = 0
        for i in range(1, len(arr)):
            num = arr[i]
            if num > res:
                res = num
                count = 0
            count += 1

            if count == k:
                # Lol LeetCode started to use mypy,
                # so I can't return here. 👎👎👎
                break

        return res

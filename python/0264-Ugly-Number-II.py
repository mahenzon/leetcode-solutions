class Solution:
    def nthUglyNumber(self, n: int) -> int:
        nums = [1]
        idx2 = 0
        idx3 = 0
        idx5 = 0

        for _ in range(1, n):
            nxt2 = nums[idx2] * 2
            nxt3 = nums[idx3] * 3
            nxt5 = nums[idx5] * 5
            nxt = min(nxt2, nxt3, nxt5)

            if nxt == nxt2:
                idx2 += 1
            if nxt == nxt3:
                idx3 += 1
            if nxt == nxt5:
                idx5 += 1
            nums.append(nxt)

        return nums[-1]

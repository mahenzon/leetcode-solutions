class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        a = 0
        b = 0
        # find max elems
        for v in nums:
            if v > a:
                a, b = v, a
            elif v > b:
                b = v

        return (a - 1) * (b - 1)

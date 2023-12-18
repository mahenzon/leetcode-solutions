class Solution:
    def maxProductDifference(self, nums: list[int]) -> int:
        min_a = 10**4
        min_b = 10**4
        max_a = 0
        max_b = 0

        for n in nums:
            # find smallest two mins
            if n < min_a:
                min_a, min_b = n, min_a
            elif n < min_b:
                min_b = n

            # find biggest two maxs
            if n > max_a:
                max_a, max_b = n, max_a
            elif n > max_b:
                max_b = n

        return max_a * max_b - min_a * min_b

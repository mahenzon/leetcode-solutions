class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [None] * n
        left = 0
        right = n - 1
        for idx in range(n - 1, -1, -1):
            left_sq = nums[left]**2
            right_sq = nums[right]**2
            if left_sq > right_sq:
                result[idx] = left_sq
                left += 1
            else:
                result[idx] = right_sq
                right -= 1
        return result

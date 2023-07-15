class Solution:
    def maxArea(self, height: List[int]) -> int:
        result = 0

        left = 0
        right = len(height) - 1

        while left < right:
            area = (right - left) * min(height[left], height[right])
            result = max(result, area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return result

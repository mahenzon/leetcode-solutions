class Solution:
    def findMin(self, nums: List[int]) -> int:
        # haha
        # return min(nums)

        left = 0
        right = len(nums) - 1

        result = nums[0]

        while left <= right:
            result = min(result, nums[left])
            # mid = (right + left) // 2
            mid = left + ((right - left) // 2)
            result = min(result, nums[mid])
            if nums[left] <= nums[mid]:
                # left is sorted
                left = mid + 1
            else:
                # right is sorted
                right = mid - 1

        return result

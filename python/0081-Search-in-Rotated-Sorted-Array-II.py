class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2
            mid_val = nums[mid]

            if mid_val == target:
                return True

            while left < mid and nums[left] == mid_val:
                left += 1

            while right > mid and nums[right] == mid_val:
                right -= 1

            left_val = nums[left]
            right_val = nums[right]
            if mid_val >= left_val:
                # left is sorted
                if left_val <= target < mid_val:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                # right is sorted
                if mid_val < target <= right_val:
                    left = mid + 1
                else:
                    right = mid - 1

        return False

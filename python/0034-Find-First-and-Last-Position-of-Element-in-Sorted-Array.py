class Solution:
    def search(self, nums: List[int], target: int, left_biased: bool) -> int:
        left = 0
        right = len(nums) - 1
        result_index = -1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                result_index = mid
                if left_biased:
                    right = mid - 1
                else:
                    left = mid + 1

        return result_index

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return [
            self.search(nums, target, left_biased=True),
            self.search(nums, target, left_biased=False),
        ]

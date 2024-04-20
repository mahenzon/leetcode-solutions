class Solution:
    def two_sum(self, start: int, target: int) -> None:
        nums = self.nums
        left = start
        right = len(nums) - 1

        while left < right:
            left_value = nums[left]
            right_value = nums[right]
            val = left_value + right_value
            if val < target:
                left += 1
            elif val > target:
                right -= 1
            else:
                self.results.append(self.prefix + [left_value, right_value])
                left += 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
    def k_sum(self, k: int, start: int, target: int) -> None:
        if k == 2:
            self.two_sum(start, target)
            return

        nums = self.nums
        for idx in range(start, len(nums) - k + 1):
            if (
                # not start
                idx > start
                and
                # not same as prev
                nums[idx] == nums[idx - 1]
            ):
                continue
            value = nums[idx]
            self.prefix.append(value)
            self.k_sum(k - 1, idx + 1, target - value)
            self.prefix.pop()

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        self.nums = nums
        self.prefix = []
        self.results = []
        self.k_sum(4, 0, target)
        return self.results

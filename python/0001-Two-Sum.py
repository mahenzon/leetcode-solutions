class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        known_numbers = {}
        for idx, num in enumerate(nums):
            desire = target - num
            if desire in known_numbers:
                return [known_numbers[desire], idx]
            known_numbers[num] = idx

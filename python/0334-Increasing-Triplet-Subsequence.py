class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = 2 ** 31
        second = 2 ** 31
        for third in nums:
            if third <= first:
                first = third
            elif third <= second:
                second = third
            else:
                return True
        return False

class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        last = 0
        for num in arr:
            last = min(last + 1, num)
        return last

# `bisect` helper is already imported in LeetCode
import bisect


class MedianFinder:

    def __init__(self):
        self.sorted_nums = []

    def addNum(self, num: int) -> None:
        bisect.insort(self.sorted_nums, num)

    def findMedian(self) -> float:
        mid = len(self.sorted_nums) // 2
        if len(self.sorted_nums) % 2:
            return self.sorted_nums[mid]
        return (self.sorted_nums[mid] + self.sorted_nums[mid - 1]) / 2

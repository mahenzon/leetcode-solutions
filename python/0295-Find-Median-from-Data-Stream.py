# `bisect` helper is already imported in LeetCode
# `heapq` helper is already imported in LeetCode
import bisect
import heapq


# slow solution, easier to implement
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


# faster solution (about 3x), harder to implement
class MedianFinder:

    def __init__(self):
        # max heap (yes). so we can take the smallest in O(1)
        self.small = []
        # min heap (yes). so we can take the largest in O(1)
        self.large = []

    def addNum(self, num: int) -> None:
        # max heap
        heapq.heappush(self.small, -num)
        # make sure all nums in small are smaller than nums in large
        if (
            self.small
            and self.large
            and -self.small[0] > self.large[0]
        ):
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        # is size uneven? fix it
        if len(self.small) > len(self.large) + 1:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        elif len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -self.small[0]
        if len(self.large) > len(self.small):
            return self.large[0]

        return (self.large[0] - self.small[0]) / 2

# `collections` is already imported in LeetCode
import collections


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        max_values_idx = collections.deque()

        for idx, num in enumerate(nums):
            # get rid of smaller values at the end of the queue
            # so we can add a bigger one to the end
            while max_values_idx and nums[max_values_idx[-1]] <= num:
                max_values_idx.pop()
            # add a bigger number index
            max_values_idx.append(idx)

            # if first elem in the queue doesn't fit in the window
            if idx - max_values_idx[0] >= k:
                # max one iteration
                max_values_idx.popleft()

            # check if we already checked k+ values
            # (fully opened our window)
            if (idx + 1) >= k:
                # the first value is the max value in the window
                res.append(nums[max_values_idx[0]])

        return res

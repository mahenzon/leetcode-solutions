class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        result = []
        idx = 0
        # insert prevs
        while idx < n and intervals[idx][1] < newInterval[0]:
            result.append(intervals[idx])
            idx += 1

        # merge overlapping (if present)
        while idx < n and intervals[idx][0] <= newInterval[1]:
            newInterval = [
                min(newInterval[0], intervals[idx][0]),
                max(newInterval[1], intervals[idx][1]),
            ]
            idx += 1

        result.append(newInterval)

        # insert the rest of intervals
        while idx < n:
            result.append(intervals[idx])
            idx += 1

        return result

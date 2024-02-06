class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # intervals.sort(key=lambda pair: pair[0])
        intervals.sort()
        output = [intervals[0]]

        # for start, end in intervals[1:]
        for idx in range(1, len(intervals)):
            start, end = intervals[idx]
            last_interval = output[-1]
            last_end = last_interval[1]

            if start > last_end:
                output.append(intervals[idx])
                # output.append([start, end])
            else:
                last_interval[1] = max(last_end, end)

        return output

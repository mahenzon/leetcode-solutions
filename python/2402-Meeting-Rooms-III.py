# `heapq` is already imported in LeetCode
import heapq


class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()

        # indexes from zero
        available = list(range(n))
        # pairs of (end_time, room_number)
        used = []
        # meetings schedules for each of the rooms
        counts = [0] * n

        for start, end in meetings:
            # end meetings
            while used and start >= used[0][0]:
                _, room_number = heapq.heappop(used)
                heapq.heappush(available, room_number)

            # if no room is available
            if not available:
                end_time, room_number = heapq.heappop(used)
                end = end_time + (end - start)
                heapq.heappush(available, room_number)

            room_number = heapq.heappop(available)
            heapq.heappush(used, (end, room_number))
            counts[room_number] += 1

        result_idx = 0
        max_value = counts[result_idx]
        for idx, count in enumerate(counts):
            if count > max_value:
                max_value = count
                result_idx = idx
        return result_idx

# `heapq` is already imported in LeetCode
import heapq


class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = []
        for building_idx in range(len(heights) - 1):
            diff = heights[building_idx + 1] - heights[building_idx]
            if diff <= 0:
                continue
            heapq.heappush(heap, diff)
            if len(heap) > ladders:
                min_diff = heapq.heappop(heap)
                bricks -= min_diff
                if bricks < 0:
                    return building_idx

        return len(heights) - 1

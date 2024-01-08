# `heapq` helper is already imported in LeetCode
import heapq


class Solution:
    def get_height(self) -> int:
        if not self.heights_heap:
            return 0
        return -self.heights_heap[0][0]

    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        if not buildings:
            return []

        n = len(buildings)
        if n == 1:
            # buildings[i] = [lefti, righti, heighti]
            left, right, height = buildings[0]
            return [[left, height], [right, 0]]

        result = []
        self.heights_heap = []
        left_low = buildings[0][0]

        for left, right, height in buildings:
            if not height:
                continue

            while self.heights_heap and self.heights_heap[0][1] < left:
                height_inv, right_ = heapq.heappop(self.heights_heap)
                if right_ > left_low:
                    result.append([left_low, -height_inv])
                    left_low = right_

            if left_low < left and (lower_height := self.get_height()) < height:
                result.append([left_low, lower_height])
                left_low = left

            while self.get_height() == height:
                right = max(right, heapq.heappop(self.heights_heap)[1])
            heapq.heappush(self.heights_heap, (-height, right))

        while self.heights_heap:
            height_inv, right_ = heapq.heappop(self.heights_heap)
            if right_ > left_low:
                if not result or result[-1][1] != -height_inv:
                    result.append([left_low, -height_inv])
                left_low = right_

        result.append([left_low, 0])
        return result

# `heapq` is already imported in LeetCode
import heapq


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False

        counts = {}
        for n in hand:
            counts[n] = counts.get(n, 0) + 1

        m_heap = list(counts.keys())
        heapq.heapify(m_heap)
        while m_heap:
            first = m_heap[0]

            for num in range(first, first + groupSize):
                if num not in counts:
                    return False

                counts[num] -= 1
                if not counts[num]:
                    if num != m_heap[0]:
                        return False
                    heapq.heappop(m_heap)

        return True

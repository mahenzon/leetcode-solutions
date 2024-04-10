# `collections` is already imported in LeetCode
import collections


class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        result = [0] * len(deck)
        q = collections.deque(range(len(deck)))
        for card in deck:
            idx = q.popleft()
            result[idx] = card
            if q:
                q.append(q.popleft())

        return result

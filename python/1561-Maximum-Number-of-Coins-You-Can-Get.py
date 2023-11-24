# T: O(n log n)
# M: O(1)

class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        left = 0
        right = len(piles) - 1
        result = 0
        while left < right:
            # Alice
            right -= 1
            # me
            result += piles[right]
            right -= 1
            # Bob
            left += 1

        return result


# T: O(n log n)
# M: O(n)

class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        q_piles = collections.deque(sorted(piles))

        result = 0
        while q_piles:
            # Alice
            q_piles.pop()
            # me
            result += q_piles.pop()
            # Bob
            q_piles.popleft()

        return result


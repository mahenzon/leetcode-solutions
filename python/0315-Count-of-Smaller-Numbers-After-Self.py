class FenwickTree:
    """
    A Fenwick tree or binary indexed tree (BIT)
    is a data structure that can efficiently update values
    and calculate prefix sums in an array of values.

    https://en.wikipedia.org/wiki/Fenwick_tree
    """

    def __init__(self, n: int):
        self.sums = [0] * (n + 1)

    @classmethod
    def low_bit(cls, i: int) -> int:
        return i & -i

    def get(self, i: int) -> int:
        total = 0
        while i > 0:
            total += self.sums[i]
            i -= self.low_bit(i)
        return total

    def update(self, i: int, delta: int) -> None:
        while i < len(self.sums):
            self.sums[i] += delta
            i += self.low_bit(i)


class Solution:
    def get_ranks(self, nums: List[int]) -> dict[int, int]:
        ranks = {}
        rank = 0

        for num in sorted(set(nums)):
            rank += 1
            ranks[num] = rank

        return ranks

    def countSmaller(self, nums: List[int]) -> List[int]:
        result = []
        num_to_rank = self.get_ranks(nums)
        tree = FenwickTree(len(num_to_rank))

        for num in reversed(nums):
            result.append(tree.get(num_to_rank[num] - 1))
            tree.update(num_to_rank[num], 1)

        return reversed(result)

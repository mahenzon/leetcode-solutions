class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        times = minutesToTest / minutesToDie + 1
        result = 0
        while times ** result < buckets:
            result += 1

        return result

class Solution:
    def isUgly(self, n: int) -> bool:
        if n < 1:
            return False

        for factor in (2, 3, 5):
            while n % factor == 0:
                n //= factor

        return n == 1

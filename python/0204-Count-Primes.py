# `math` is already imported in LeetCode
import math


class Solution:
    def sieve_of_eratosthenes(self, num):
        is_prime = [True] * num
        is_prime[0] = False
        is_prime[1] = False

        for n in range(2, int(math.sqrt(num)) + 1):
            if is_prime[n]:
                for i in range(n * n, num, n):
                    is_prime[i] = False

        return is_prime

    def countPrimes(self, n: int) -> int:
        if n < 3:
            return 0

        return sum(self.sieve_of_eratosthenes(n))

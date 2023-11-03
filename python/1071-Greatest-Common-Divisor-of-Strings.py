from math import gcd  # is imported by default on LeetCode


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""

        max_len_gcd = gcd(len(str1), len(str2))
        return str1[:max_len_gcd]

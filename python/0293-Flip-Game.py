"""
LeetCode: https://leetcode.com/problems/flip-game
LintCode: https://www.lintcode.com/problem/914/
"""

from typing import (
    List,
)

class Solution:
    def generate_possible_next_moves(self, s: str) -> List[str]:
        """
        @param s: the given string
        @return: all the possible states of the string after one valid move
                we will sort your return value in output
        """
        res = []
        for i in range(1, len(s)):
            l = i - 1
            r = i + 1
            if s[l:r] == "++":
                res.append(f"{s[:l]}--{s[r:]}")
        return res

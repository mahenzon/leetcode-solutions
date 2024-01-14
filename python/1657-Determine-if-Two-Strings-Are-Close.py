# `collections` is already imported in LeetCode
import collections


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False

        count1 = collections.Counter(word1)
        count2 = collections.Counter(word2)

        # no new chars, otherwise aren't close

        # if count of 'b' is 2 and count of 'a' is 1
        # and in the second word it's reversed (b=1, a=2),
        # then we can swap them in one operation
        return (
            count1.keys() == count2.keys() and
            sorted(count1.values()) == sorted(count2.values())
        )

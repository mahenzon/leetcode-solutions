# `string` is already imported in LeetCode
import string


class Solution:
    def customSortString(self, order: str, s: str) -> str:
        chars = [0] * 26
        result = []
        for c in s:
            chars[ord(c) - ord("a")] += 1
        for c in order:
            pos = ord(c) - ord("a")
            if count := chars[pos]:
                result.append(c * count)
                chars[pos] = 0

        for c in string.ascii_lowercase:
            pos = ord(c) - ord("a")
            if count := chars[pos]:
                result.append(c * count)

        return "".join(result)

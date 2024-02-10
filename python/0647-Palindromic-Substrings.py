class Solution:
    def get_pali_count(self, left: int, right: int) -> int:
        count = 0
        while (
            # left in bounds
            left >= 0
            and
            # right in bounds
            right < len(self. s)
            and
            # chars are equal - is palindrome
            self.s[left] == self.s[right]
        ):
            count += 1
            left -= 1
            right += 1
        return count

    def countSubstrings(self, s: str) -> int:
        self.s = s
        result = 0
        for idx in range(len(s)):
            result += self.get_pali_count(idx, idx)
            result += self.get_pali_count(idx, idx + 1)
        return result

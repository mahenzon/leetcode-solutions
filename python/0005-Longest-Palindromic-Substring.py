class Solution:

    def find_and_set_longest_palindrome(self, left: int, right: int) -> str:
        while left >= 0 and right < len(self.s) and self.s[left] == self.s[right]:
            left -= 1
            right += 1

        pal = self.s[left + 1:right]
        if len(pal) > len(self.result):
            self.result = pal

    def longestPalindrome(self, s: str) -> str:
        self.s = s
        self.result = ""

        for idx in range(len(s)):
            # odd len
            self.find_and_set_longest_palindrome(idx, idx)
            # even len
            self.find_and_set_longest_palindrome(idx, idx + 1)

        return self.result

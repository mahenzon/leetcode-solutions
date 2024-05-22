class Solution:
    def is_palindrome(self, left, right) -> bool:
        while left < right:
            if self.s[left] != self.s[right]:
                return False
            left += 1
            right -= 1
        return True

    def dfs(self, parts, idx) -> None:
        if idx >= len(self.s):
            self.result.append(parts.copy())
            return
        for i in range(idx, len(self.s)):
            if self.is_palindrome(idx, i):
                next_idx = i + 1
                parts.append(self.s[idx:next_idx])
                self.dfs(parts, next_idx)
                parts.pop()

    def partition(self, s: str) -> List[List[str]]:
        self.s = s
        self.result = []
        self.dfs([], 0)
        return self.result

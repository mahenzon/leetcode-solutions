class Solution:
    def overlap(self, line: str) -> bool:
        known = set()
        for c in line:
            if c in self.chars or c in known:
                return True
            known.add(c)
        return False

    def backtrack(self, idx: int) -> int:
        if idx == len(self.arr):
            return len(self.chars)

        res = 0
        line = self.arr[idx]
        if not self.overlap(line):
            self.chars.update(line)
            res = self.backtrack(idx + 1)
            self.chars.difference_update(line)

        return max(res, self.backtrack(idx + 1))

    def maxLength(self, arr: List[str]) -> int:
        self.chars = set()
        self.arr = arr
        return self.backtrack(0)

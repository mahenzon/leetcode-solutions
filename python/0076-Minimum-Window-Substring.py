class Solution:
    def minWindow(self, s: str, t: str) -> str:
        counts = {}
        for c in t:
            counts[c] = counts.get(c, 0) + 1
        chars_needed = len(t)
        best_left = -1
        min_length = len(s) + 1

        left = 0
        for right, char in enumerate(s):
            if char not in counts:
                continue
            counts[char] -= 1
            if counts[char] >= 0:
                chars_needed -= 1
            while not chars_needed:
                if (size := right - left + 1) < min_length:
                    best_left = left
                    min_length = size
                left_char = s[left]
                left += 1
                if left_char not in counts:
                    continue
                counts[left_char] += 1
                if counts[left_char] > 0:
                    chars_needed += 1

        if best_left == -1:
            return ""
        return s[best_left: best_left + min_length]

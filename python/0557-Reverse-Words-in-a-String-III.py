class Solution:
    def reverseWords(self, s: str) -> str:
        line = list(s)
        left = 0
        line_len = len(line)
        for right in range(line_len):
            is_last_char = right == line_len - 1
            if not (is_last_char or line[right] == " "):
                continue

            l = left
            r = right - 1
            if is_last_char:
                r = right

            while l < r:
                line[l], line[r] = line[r], line[l]
                l += 1
                r -= 1

            left = right + 1

        return "".join(line)

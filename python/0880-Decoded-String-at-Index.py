class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        length = 0
        idx = 0

        while length < k:
            char = s[idx]
            if char.isdigit():
                length *= int(char)
            else:
                length += 1
            idx += 1

        while idx:
            idx -= 1
            char = s[idx]
            if char.isdigit():
                length //= int(char)
                k %= length
            else:
                if k == length or k == 0:
                    return char
                length -= 1

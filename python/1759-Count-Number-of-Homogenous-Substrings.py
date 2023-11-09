class Solution:
    def countHomogenous(self, s: str) -> int:
        modulo = 10 ** 9 + 7
        res = 0
        count = 0
        last_char = ""

        for char in s:
            if char == last_char:
                count += 1
            else:
                count = 1
                last_char = char
            res += count

        return res % modulo

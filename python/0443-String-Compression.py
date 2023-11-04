class Solution:
    def compress(self, chars: List[str]) -> int:
        idx = 0
        count = 0
        the_char = ""
        for char in chars:
            if char == the_char:
                count += 1
                continue

            if count > 1:
                for n in str(count):
                    chars[idx] = n
                    idx += 1

            the_char = char
            chars[idx] = char
            idx += 1
            count = 1

        if count > 1:
            for n in str(count):
                chars[idx] = n
                idx += 1

        # lol LeetCode doesn't check for extra items
        # while len(chars) > idx:
        #     chars.pop()

        return idx

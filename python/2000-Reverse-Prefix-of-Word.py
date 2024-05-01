class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        word = list(word)

        for idx, char in enumerate(word, start=1):
            if char != ch:
                continue

            prefix = word[:idx]
            prefix.reverse()
            word[:idx] = prefix
            break

        return "".join(word)

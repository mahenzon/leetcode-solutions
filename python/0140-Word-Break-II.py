class Solution:
    def break_words(self, s: str) -> List[str]:
        if s in self.cache:
            return self.cache[s]

        res = []
        for i in range(1, len(s)):
            prefix = s[0:i]
            suffix = s[i:]
            if prefix not in self.words:
                continue
            for word in self.break_words(suffix):
                res.append(f"{prefix} {word}")

        if s in self.words:
            res.append(s)

        self.cache[s] = res
        return res

    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        self.cache = {}
        self.words = set(wordDict)
        return self.break_words(s)

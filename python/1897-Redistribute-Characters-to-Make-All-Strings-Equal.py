class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        counts = {}
        for word in words:
            for char in word:
                counts[char] = counts.get(char, 0) + 1

        words_count = len(words)
        for count in counts.values():
            if count % words_count:
                return False
        return True

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        fragments = []

        min_len = min(len(word1), len(word2))
        for i in range(min_len):
            fragments.append(word1[i])
            fragments.append(word2[i])

        # add leftovers
        fragments.append(word1[min_len:])
        fragments.append(word2[min_len:])
        return "".join(fragments)

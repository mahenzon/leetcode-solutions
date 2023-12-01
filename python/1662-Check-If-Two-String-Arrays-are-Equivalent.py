class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        w1 = 0
        w2 = 0
        idx_1 = 0
        idx_2 = 0

        w1_len = len(word1)
        w2_len = len(word2)

        while w1 < w1_len and w2 < w2_len:
            if word1[w1][idx_1] != word2[w2][idx_2]:
                return False

            idx_1 += 1
            idx_2 += 1

            if idx_1 == len(word1[w1]):
                w1 += 1
                idx_1 = 0

            if idx_2 == len(word2[w2]):
                w2 += 1
                idx_2 = 0

        return w1 == w1_len and w2 == w2_len

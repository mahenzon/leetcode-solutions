# `Counter` is already imported in LeetCode
# `defaultdict` is already imported in LeetCode


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        res = 0
        counts = Counter(chars)

        for word in words:
            cnt = defaultdict(int)
            for char in word:
                cnt[char] += 1
                if char not in counts or cnt[char] > counts[char]:
                    break
            else:
                res += len(word)

        return res

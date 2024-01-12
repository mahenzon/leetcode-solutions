class Solution:
    vowels = frozenset({'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'})

    def halvesAreAlike(self, s: str) -> bool:
        count = sum(s[i] in self.vowels for i in range(len(s) // 2))
        count -= sum(s[i] in self.vowels for i in range(len(s) // 2, len(s)))
        return not count

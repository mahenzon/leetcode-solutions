class Solution:
    vowels = {
        "a", "A",
        "e", "E",
        "i", "I",
        "o", "O",
        "u", "U",
    }

    def sortVowels(self, s: str) -> str:
        vowels_sorted = sorted([c for c in s if c in self.vowels])
        result = []
        idx = 0

        for char in s:
            if char in self.vowels:
                result.append(vowels_sorted[idx])
                idx += 1
            else:
                result.append(char)

        return "".join(result)

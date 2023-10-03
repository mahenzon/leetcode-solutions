class Solution:
    def reverseVowels(self, s: str) -> str:
        left = 0
        right = len(s) - 1
        line = list(s)

        vowels = {"a", "e", "i", "o", "u"}

        while left < right:
            if line[left].lower() not in vowels:
                left += 1
            elif line[right].lower() not in vowels:
                right -= 1
            else:
                line[left], line[right] = line[right], line[left]

                left += 1
                right -= 1

        return "".join(line)

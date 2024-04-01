class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # return len(s.strip().split(" ")[-1])
        count = 0
        last_count = 0
        for c in s:
            if c == " ":
                count = 0
                continue
            count += 1
            last_count = count

        return last_count

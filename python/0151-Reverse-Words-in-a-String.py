class Solution:
    def reverseWords(self, s: str) -> str:
        last = 0
        pointer = 0
        s_len = len(s)

        # we could use deque to add to start,
        # so we could eliminate the 'reverse' step
        words = []
        while pointer < s_len:
            if s[pointer] == " ":
                if pointer - last > 0:
                    # append word to list
                    words.append(s[last:pointer])
                last = pointer + 1

            pointer += 1

        # if the last char wasn't space,
        # we need to add the last word
        if s[pointer - 1] != " ":
            words.append(s[last:pointer])

        # idk if there's a better way to reverse
        return " ".join(words[::-1])

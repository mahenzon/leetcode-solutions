class Solution:

    def get_next_char_index(self, line: str, index: int) -> int:
        # next is actually prev
        steps_back = 0
        while index >= 0:
            if steps_back == 0 and line[index] != "#":
                break

            if line[index] == "#":
                steps_back += 1
            else:
                steps_back -= 1

            index -= 1
        return index

    def get_char(self, line, index) -> str:
        if index < 0:
            return ""
        return line[index]

    def backspaceCompare(self, s: str, t: str) -> bool:
        index_s = len(s)
        index_t = len(t)

        while index_s > 0 or index_t > 0:
            index_s -= 1
            index_t -= 1

            index_s = self.get_next_char_index(s, index_s)
            index_t = self.get_next_char_index(t, index_t)

            char_s = self.get_char(s, index_s)
            char_t = self.get_char(t, index_t)

            if char_s != char_t:
                return False

        return True

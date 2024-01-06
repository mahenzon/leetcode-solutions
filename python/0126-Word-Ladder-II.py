# `collections` and `string` are already imported in LeetCode
import collections
import string


class Solution:

    def get_next_words(self, word) -> List[str]:
        words = []
        # work on the last word in the path
        word_chars = list(word)
        for idx, orig_char in enumerate(word_chars):
            # replace char in word with all known letters (by one)
            for char in string.ascii_lowercase:
                if char == orig_char:
                    continue
                word_chars[idx] = char
                # build new word based on new chars
                new_word = "".join(word_chars)
                # if we have this word in word_set, use
                if new_word in self.word_set:
                    words.append(new_word)
            # recover word
            word_chars[idx] = orig_char

        return words

    def fill_distances(self):
        # distance to end is zero
        self.distances[self.end_word] = 0
        reverse_transformations = collections.deque()
        # start from end_word
        reverse_transformations.append(self.end_word)
        # go through all options
        while reverse_transformations:
            word = reverse_transformations.popleft()
            for new_word in self.get_next_words(word):
                if new_word in self.distances:
                    continue
                self.distances[new_word] = self.distances[word] + 1
                reverse_transformations.append(new_word)

    def backtrack(self, start: str, path: List[str]) -> None:
        if start == self.end_word:
            self.res.append(list(path))
            return
        # skip if this word is not in the path to the end
        if start not in self.distances:
            return
        for new_word in self.get_next_words(start):
            # should be closer to the end by one step from current start
            desired_distance = self.distances[start] - 1
            if self.distances[new_word] != desired_distance:
                continue
            path.append(new_word)
            self.backtrack(new_word, path)
            path.pop()

    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        self.word_set = set(wordList)
        if endWord not in self.word_set:
            return []

        # make sure we can backtrack to the start
        self.word_set.add(beginWord)

        self.end_word = endWord
        self.distances = {}
        self.fill_distances()
        self.res = []
        self.backtrack(beginWord, [beginWord])

        return self.res

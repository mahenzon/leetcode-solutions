# `collections` and `string` are already imported in LeetCode
import collections
import string


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)
        if endWord not in word_set:
            return 0

        transformations = collections.deque()
        # start with beginWord
        transformations.append(beginWord)

        res = 0
        while transformations:
            # start new transformation step
            res += 1
            # try all options in this transformation step
            for _ in range(len(transformations)):
                word_chars = list(transformations.popleft())
                for idx, orig_char in enumerate(word_chars):
                    for new_char in string.ascii_lowercase:
                        word_chars[idx] = new_char
                        new_word = "".join(word_chars)
                        if new_word == endWord:
                            return res + 1
                        if new_word in word_set:
                            # use this word on the next iteration
                            transformations.append(new_word)
                            # don't get back to this word ever again
                            word_set.remove(new_word)
                    word_chars[idx] = orig_char

        return 0

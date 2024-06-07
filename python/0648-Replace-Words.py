class Solution:
    word_key = 'word'

    def add(self, word: str) -> None:
        node = self.graph
        for char in word:
            if char not in node:
                node[char] = {}
            node = node[char]
        node[self.word_key] = word

    def search(self, word: str) -> str:
        node = self.graph
        for char in word:
            if self.word_key in node:
                return node[self.word_key]
            if char not in node:
                return word
            node = node[char]
        return word

    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        self.graph = {}

        for word in dictionary:
            self.add(word)

        words = sentence.split(' ')
        return ' '.join(self.search(word) for word in words)

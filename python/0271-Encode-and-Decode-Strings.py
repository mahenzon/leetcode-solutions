class Solution:
    def encode(self, strings):
        """
        @param: strings: a list of strings
        @return: encodes a list of strings to a single string.
        """
        delimiter = "|"
        result = ""
        for word in strings:
            result += "{count}{delimiter}{word}".format(
                count=len(word), delimiter=delimiter, word=word)
        return result

    def decode(self, string):
        """
        @param: string: A string
        @return: decodes a single string to a list of strings
        """
        delimiter = "|"
        result = []
        last_char_pos = 0
        string_len = len(string)
        while last_char_pos < string_len:
            num_pos = last_char_pos

            while string[num_pos] != delimiter:
                num_pos += 1

            word_len = int(string[last_char_pos:num_pos])
            word_start = num_pos + 1
            word_end = word_start + word_len
            word = string[word_start:word_end]

            result.append(word)
            last_char_pos = word_end

        return result

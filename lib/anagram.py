class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, l):
        split_word = list(self.word)
        split_word.sort()
        match_list = []
        for word in l:
            split_match = list(word)
            split_match.sort()
            if(split_match == split_word):
                match_list.append(word)
        return match_list
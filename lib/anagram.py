class Anagram():
    def __init__(self, word):
        self.word = word

    def match(self, words_list):
        anagrams = []
        for item in words_list:
            if sorted([letter for letter in item]) == sorted([letter for letter in self.word]):
                anagrams.append(item)
        return anagrams
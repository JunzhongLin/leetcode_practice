'''
The abbreviation of a word is a concatenation of its first letter, the number of characters between the first and last letter, and its last letter. If a word has only two characters, then it is an abbreviation of itself.

For example:

dog --> d1g because there is one letter between the first letter 'd' and the last letter 'g'.
internationalization --> i18n because there are 18 letters between the first letter 'i' and the last letter 'n'.
it --> it because any word with only two characters is an abbreviation of itself.
Implement the ValidWordAbbr class:

ValidWordAbbr(String[] dictionary) Initializes the object with a dictionary of words.
boolean isUnique(string word) Returns true if either of the following conditions are met (otherwise returns false):
There is no word in dictionary whose abbreviation is equal to word's abbreviation.
For any word in dictionary whose abbreviation is equal to word's abbreviation, that word and word are the same.


'''


class ValidWordAbbr(object):

    def __init__(self, dictionary):
        """
        :type dictionary: List[str]
        """
        self.hash_map = collections.defaultdict(list)
        self.word_set = set()
        for word in dictionary:
            abbrev = self._gen_abbrev(word)
            if word not in self.word_set:
                self.hash_map[abbrev].append(word)
            self.word_set.add(word)

    def _gen_abbrev(self, word):
        if len(word) <= 2:
            return word
        return word[0] + str(len(word) - 2) + word[-1]

    def isUnique(self, word):
        """
        :type word: str
        :rtype: bool
        """
        abbrev = self._gen_abbrev(word)
        if word in self.word_set and len(self.hash_map[abbrev]) < 2:
            return True
        if abbrev not in self.hash_map:
            return True

        return False
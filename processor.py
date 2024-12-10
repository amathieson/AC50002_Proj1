import re
from itertools import combinations

from PrioritySet import PrioritySet


class algo(object):
    def __init__(self, letter_scores):
        self.letterScores = letter_scores

    def generate_set(self, words):
        acronyms = dict()
        for word in words:
            acronyms[word] = self.generate_acronyms(word)
        acronym_words = dict()
        for i, word in enumerate(words):
            for j, word2 in enumerate(words):
                if i != j:
                    intersect = acronyms[word].intersection(acronyms[word2])
                    for e in intersect:
                        acronyms[word].remove(e)
                        acronyms[word2].remove(e)
        for word in words:
            explore = True
            acronym_words[word] = []
            word_pri, acro = acronyms[word].pop()
            if acro is not None:
                acronym_words[word].append(acro)
                while explore:
                    pri, d = acronyms[word].pop()
                    if pri == word_pri:
                        acronym_words[word].append(d)
                    else:
                        explore = False
            else:
                acronym_words[word] = None

        return acronym_words

    def generate_acronyms(self, word):
        upper_word = word.upper()
        letters = upper_word[1:]
        acronyms = PrioritySet()

        for letter, letter2 in combinations(letters, 2):
            acronym = upper_word[0] + letter + letter2
            scr = self.score(upper_word, acronym)
            if scr != -1:
                acronyms.add(acronym, scr)
        return acronyms

    def score(self, word, acronym):
        if word[0] != acronym[0]:
            return -1
        acroScore = 0
        words = re.split('[^A-Z\']', word)
        used_letters = {(0, 0)}
        for letter in acronym[1:]:
            if letter == "'":
                return -1
            tScore = float('inf')
            letter_index = None
            for j, _word in enumerate(words):
                word_len = len(_word)
                for i, e in enumerate(_word):
                    if (j, i) in used_letters:
                        continue
                    if e == letter:
                        if i == 0 and tScore > 0:
                            tScore = 0
                            letter_index = (j, 0)
                            break
                        if i == word_len - 1:
                            if letter == 'E' and tScore > 20:
                                tScore = 20
                                letter_index = (j, word_len - 1)
                            else:
                                if tScore > 5:
                                    tScore = 5
                                    letter_index = (j, word_len - 1)
                        a = min(i, 3) + self.letterScores[letter]
                        if tScore > a:
                            tScore = a
                            letter_index = (j, i)
            if letter_index is not None:
                acroScore += tScore
                used_letters.add(letter_index)
            else:
                return -1
        return acroScore

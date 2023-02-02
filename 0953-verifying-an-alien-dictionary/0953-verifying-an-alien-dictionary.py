class Solution:
    def isAlienSorted(self, words, order):
        dic = {c: i for i, c in enumerate(order)}
        words = [[dic[c] for c in w] for w in words]
        return all(x <= y for x, y in zip(words, words[1:]))
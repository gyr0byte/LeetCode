class Solution(object):
    def findWordsContaining(self, words, x):
        idx = []
        for i in range(len(words)):
            if x in words[i]:
                idx.append(i)
        return idx
        
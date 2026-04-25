class Solution(object):
    def minDistance(self, word1, word2):
        memo = {}
        def recurse(i1, i2):
            key = i1, i2
            if key in memo:
                return memo[key]
            elif i1 == len(word1):
                memo[key] = len(word2) - i2
            elif i2 == len(word2):
                memo[key] = len(word1) - i1
            elif word1[i1] == word2[i2]:
                memo[key] = recurse(i1+1,i2+1)
            else:
                memo[key] = 1 + min(recurse(i1 + 1, i2), recurse(i1+1,i2+1), recurse(i1, i2+1))
            return memo[key]
        return recurse(0, 0)
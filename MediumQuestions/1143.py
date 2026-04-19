class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        memo = {}
        def recurse(idx1 = 0, idx2 = 0):
            key = (idx1, idx2)
            if key in memo:
                return memo[key]
            if idx1 == len(text1) or idx2 == len(text2):
                memo[key] = 0
            elif text1[idx1] == text2[idx2]:
                memo[key] = 1 + recurse(idx1 + 1, idx2 + 1)
            else:
                memo[key] = max(recurse(idx1 + 1, idx2), recurse(idx1, idx2 + 1))
            return memo[key]
        return recurse(0,0)
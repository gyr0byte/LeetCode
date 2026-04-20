class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        n1, n2 = len(text1), len(text2)
        table = [[0 for x in range(n2+1)] for x in range(n1+1)]
        for idx1 in range(n1):
            for idx2 in range(n2):
                if text1[idx1] == text2[idx2]:
                    table[idx1+1][idx2+1] = 1 + table[idx1][idx2]
                else:
                    table[idx1+1][idx2+1] = max(table[idx1][idx2+1], table[idx1+1][idx2])

        return table[-1][-1]
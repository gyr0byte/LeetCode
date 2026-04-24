class Solution(object):
    def reverseDegree(self, s):
        deg = 0
        for i, ch in enumerate(s):
            reverse_pos = 26 - (ord(ch) - ord('a'))
            deg += reverse_pos * (i + 1)
        return deg
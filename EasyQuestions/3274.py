class Solution(object):
    def checkTwoChessboards(self, coordinate1, coordinate2):
        val1 = ord(coordinate1[0]) + int(coordinate1[1])
        val2 = ord(coordinate2[0]) + int(coordinate2[1])
        return True if (val1%2 == 0 and val2%2 == 0) == (val1%2 == 0) else False
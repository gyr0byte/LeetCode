class Solution(object):
    def lengthOfLastWord(self, s):
        lst = s.strip().split(" ")
        return len(lst[-1])
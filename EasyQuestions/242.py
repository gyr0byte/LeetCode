class Solution(object):
    def isAnagram(self, s, t):
        alpha = "abcdefghijklmnopqrstuvwxyz"
        for letter in alpha:
            if s.count(letter) != t.count(letter):
                return False
        return True

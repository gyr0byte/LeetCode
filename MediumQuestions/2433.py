class Solution(object):
    def findArray(self, pref):
        arr = []
        arr.append(pref[0])
        for i in range(len(pref) - 1):
            comp = pref[i] ^ pref[i+1]
            arr.append(comp)
        return arr
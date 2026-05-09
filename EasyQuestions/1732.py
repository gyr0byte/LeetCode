class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        alt = 0
        gain_count = 0
        for i in range(len(gain)):
            gain_count += gain[i]
            if gain_count > alt:
                alt = gain_count
        return alt
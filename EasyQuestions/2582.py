class Solution(object):
    def passThePillow(self, n, time):
        cycle = 2 * (n - 1)
        time %= cycle
        if time < n:
            return 1 + time
        else:
            return n - (time - (n - 1))
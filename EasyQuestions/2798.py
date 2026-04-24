class Solution(object):
    def numberOfEmployeesWhoMetTarget(self, hours, target):
        out = 0
        for i in range(len(hours)):
            if hours[i] >= target:
                out += 1
        return out
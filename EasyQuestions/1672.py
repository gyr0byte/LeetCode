class Solution(object):
    def maximumWealth(self, accounts):
        wealth = 0
        for i in range(len(accounts)):
            salary = 0
            for j in range(len(accounts[0])):
                salary += accounts[i][j]
            if wealth < salary:
                wealth = salary
        return wealth
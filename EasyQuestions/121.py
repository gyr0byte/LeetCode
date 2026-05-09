class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price,max_profit = prices[0],0
        for price in prices:
            if price < min_price:
                min_price = price
            profit = price - min_price
            if max_profit < profit:
                max_profit = profit
        return max_profit
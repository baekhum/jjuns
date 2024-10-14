class Solution(object):
    def maxProfit(self, prices):
        min_price = prices[0]
        max_profit = 0
        for price in prices:
            profit = price - min_price
            max_profit = max(profit, max_profit)
            min_price = min(price, min_price)
            
        return max_profit
        
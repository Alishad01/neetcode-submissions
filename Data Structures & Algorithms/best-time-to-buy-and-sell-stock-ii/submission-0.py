class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i in range(len(prices)-1):
            profit = prices[i+1] - prices[i]
            max_profit = max_profit if max_profit > (max_profit + profit) else (max_profit + profit)
        return max_profit
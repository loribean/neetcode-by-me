class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        l,r = 0,1
        max_profit = 0

        while r < len(prices):
            profit = prices[r] - prices[l]
            max_profit = max(max_profit, profit)

            if profit < 0: # we make  a loss, but also means r is less than l, we found our new min
                l = r
                r += 1
            else:
                r += 1
        return max_profit
        
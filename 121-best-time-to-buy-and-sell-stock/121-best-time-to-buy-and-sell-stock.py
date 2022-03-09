class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # profit = 0
        # for i in range(len(prices)):
        #     j = i + 1
        #     while  j < len(prices):
        #         if profit < prices[j] - prices[i]:
        #             profit = prices[j] - prices[i]
        #         j = j + 1
        # return profit
        min_price = float('inf')
        max_profit = 0
        for i in range(len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            elif prices[i] - min_price > max_profit:
                max_profit = prices[i] - min_price
        return max_profit
             
        
class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        buyDate = 0
        minDate = 0
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] - prices[buyDate] > profit:
                profit = prices[i] - prices[buyDate]
            if prices[i] < prices[minDate]:
                minDate = i
            if prices[i] - prices[minDate] > profit:
                profit = prices[i] - prices[minDate]
                buyDate = minDate

        return profit

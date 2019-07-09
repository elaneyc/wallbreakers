class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        return self.maxProfitDynamic(prices)

    def maxProfitDynamic(self, prices):
        if len(prices) < 2:
            return 0

        max = 0
        min = prices[0]

        for p in prices:
            if p < min:
                min = p

            profit = p - min
            if profit > max:
                max = profit

        return max

        

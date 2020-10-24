

class Solution(object):
    def maxProfit_bad(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        res = 0
        if not prices:
            return 0
        l = len(prices)
        for i in range(l):
            for j in range(i, l):
                if res < prices[j] - prices[i]:
                    res = prices[j] - prices[i]
        return res

    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        res = 0
        if not prices:
            return 0
        l = len(prices)
        m = float('inf')
        for i in range(l):
            if prices[i] < m:
                m = prices[i]
            if prices[i] - m > res:
                res = prices[i] - m
        return res

    def maxProfit2(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0

        buy, sell = -prices[0], 0
        for i in prices[1:]:
            buy = max(buy, -i)
            sell = max(sell, buy + i)

        return sell

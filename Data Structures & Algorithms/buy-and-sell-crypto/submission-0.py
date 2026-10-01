class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #initialize the lowest and the best value
        # subtract both to get the max profit

        lo, mpr = prices[0], 0

        for price in prices:
            if price < lo:
                lo = price
            mpr = max(price-lo, mpr)
        return mpr
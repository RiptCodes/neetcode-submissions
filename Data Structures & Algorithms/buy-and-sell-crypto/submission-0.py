class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        temp = float("inf")
        profit = 0
        for price in prices:
            if price < temp:
                 temp = price
            elif price - temp > profit:
                profit = price - temp
        return profit
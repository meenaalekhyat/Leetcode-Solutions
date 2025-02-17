class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low, high=float('inf'),0
        buy, sell=-1, -1
        profit=0
        for i in range (len(prices)):
            if prices[i]<low:
                low=prices[i]
                buy=i

            profit=prices[i]-low

            if profit>high:
                high=profit
                sell=i
        return high
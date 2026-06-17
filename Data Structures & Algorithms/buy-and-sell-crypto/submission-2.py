class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best = 0
        for i in range(len(prices)-1):
            for j in range(i+1, len(prices)):
                if prices[i]>=prices[j]:
                    continue
                current = prices[j]-prices[i]
                best = max(best, current)
        return best
                
        
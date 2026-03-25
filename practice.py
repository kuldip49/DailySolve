class Solution:
    def maxProfit(prices: list[int]):
        profit = 0
        for i in range(1,len(prices)):
            if prices[i-1] < prices[i]:
                profit += (prices[i]-prices[i-1])
        return profit


print(Solution.maxProfit([7,1,5,3,6,4]))
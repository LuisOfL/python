class Solution(object):
    def maxProfit(self, prices):
        min = float("inf")
        gan = 0
        ganM = 0
        for x in prices:
            if x < min:
                min = x
            else:
                gan = x-min
                if gan > ganM:
                    ganM = gan
        return ganM


sol = Solution()
prices = [1,4,1,4,3,1]
print(sol.maxProfit(prices))

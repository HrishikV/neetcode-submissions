from functools import lru_cache
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n= len(prices)
        
        @lru_cache(None)
        def  dfs(day,holding):
            if day >=n:
                return 0
            best =dfs(day+1,holding)

            if holding:
                sell=prices[day]+dfs(day+2,False)
                best=max(sell,best)
            else:
                buy =- prices[day]+dfs(day+1,True)
                best= max(best,buy)
            return best
        return dfs(0,False)
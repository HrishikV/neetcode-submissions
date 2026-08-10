class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        sol={}
        for i in nums:
            if i not in sol:
                sol[i]=0
            sol[i]+=1
        return sorted(sol, key=sol.get, reverse=True)[:k]
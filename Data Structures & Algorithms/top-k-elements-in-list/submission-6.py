class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans=defaultdict(int)
        for i in nums:
            ans[i]+=1
        return sorted(ans.keys(),key=ans.get,reverse= True)[:k]
        
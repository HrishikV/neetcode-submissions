
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n=set(nums)
        return sorted(n,key=lambda x: nums.count(x),reverse=True)[:k]
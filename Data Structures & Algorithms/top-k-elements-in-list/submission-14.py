
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        n = list(counts.keys())
        return sorted(n, key=lambda x: counts[x], reverse=True)[:k]
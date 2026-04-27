class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        for i in range(n-1):
            s=target-nums[i]
            if s not in nums[i+1:]:
                continue
            return [i,nums[i+1:].index(s)+i+1]
        return []
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        s=float('-inf')
        for i in range(len(nums)):
            t=nums[i]
            s=max(s,t)
            if t <0:
                continue
            for j in range(i+1,len(nums)):
                t+=nums[j]
                s=max(s,t)
        return s
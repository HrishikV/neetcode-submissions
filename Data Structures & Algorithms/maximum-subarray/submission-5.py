class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        s=set()
        for i in range(len(nums)):
            t=nums[i]
            s.add(t)
            for j in range(i+1,len(nums)):
                if t <0:
                    break
                t+=nums[j]
                s.add(t)
        return max(s)
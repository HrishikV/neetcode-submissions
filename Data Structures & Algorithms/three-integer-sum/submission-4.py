class Solution:
    
 
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        sol=set()
        for i in range(n):
            for j in range(i+1,n-1):
                s=-(nums[i]+nums[j])
                p=tuple(sorted([nums[i],nums[j],s]))
                if s in nums[j+1:]:
                    sol.add(p)
        return [list(i) for i in sol]

        
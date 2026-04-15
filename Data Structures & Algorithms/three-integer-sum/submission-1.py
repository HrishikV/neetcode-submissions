class Solution:
    
 
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        sol=set()
        proc=set()
        for i in range(n):
            for j in range(i+1,n-1):
                p=tuple(sorted([nums[i],nums[j]]))
                if p not in proc:
                    s=-(nums[i]+nums[j])
                    proc.add(p)
                    if s in nums[j+1:]:
                        sol.add(tuple(sorted([nums[i],nums[j],s])))
        return [list(i) for i in sol]

        
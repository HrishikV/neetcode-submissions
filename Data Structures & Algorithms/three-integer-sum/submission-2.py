class Solution:
    
 
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        sol=[]
        proc=set()
        for i in range(n):
            for j in range(i+1,n-1):
                s=-(nums[i]+nums[j])
                p=tuple(sorted([nums[i],nums[j],s]))
                if p not in proc:
                    proc.add(p)
                    if s in nums[j+1:]:
                        sol.append(list(p))
        return sol

        
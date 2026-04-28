class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n= len(nums)
        pref=[1]*n 
        suf=[1]*n 
        for i,j in zip(range(1,n),range(n-2,-1,-1)):
            pref[i]=nums[i-1]*pref[i-1]
            suf[j]=nums[j+1]*suf[j+1]
            
        return [i*j for i,j in zip(pref,suf)]
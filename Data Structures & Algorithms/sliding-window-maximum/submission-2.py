class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
       l=0
       sol=[]
       while l+k<len(nums)+1:
            sol.append(max(nums[l:k+l]))
            l+=1
       return sol
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums=list(set(nums))
        nums.sort()
        tmp=[]
        sol=[]
        for i in range(len(nums)):
            if i == 0:
                tmp.append(nums[i])
            elif tmp[-1]==nums[i]-1 :
                tmp.append(nums[i])
                print(tmp)
            else:
                if len(tmp)> len(sol):
                    sol=tmp
                tmp=[nums[i]]
        return max(len(tmp),len(sol))
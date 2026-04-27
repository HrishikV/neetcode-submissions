class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sol=0
        tmp=''
        for i in s:
            if i in tmp:
                tmp=tmp[tmp.index(i)+1:]    
            tmp+=i
            sol=max(len(tmp),sol)
                
        return max(sol,len(tmp))
            
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        r=len(s1)
        l=0
        n=len(s2)
        s1=sorted(s1)
        while r<n+1:
            if s1==sorted(s2[l:r]):
                return True
            r+=1
            l+=1
        return False
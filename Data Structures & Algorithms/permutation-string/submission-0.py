class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        r=len(s1)
        l=0
        n=len(s2)

        while r<n+1:
            if sorted(s1)==sorted(s2[l:r]):
                return True
            r+=1
            l+=1
            #print(s1,sorted(s2[l:r]))
        return False
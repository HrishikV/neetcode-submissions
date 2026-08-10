class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sol={}
        
        for i in strs:
            key="".join(sorted(i))
            if not key in sol:
                sol[key]=[]
            sol[key].append(i)
        return list(sol.values())
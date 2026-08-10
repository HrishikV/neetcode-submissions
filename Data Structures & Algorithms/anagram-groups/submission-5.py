class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sol=defaultdict(list)
        
        for i in strs:
            sol["".join(sorted(i))].append(i)
        return list(sol.values())
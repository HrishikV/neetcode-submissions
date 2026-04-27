class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans=defaultdict(list)
        for i in strs:
            s=sorted(i)
            proc="".join(s)
            if proc not in list(ans.keys()):
                for j in strs:
                    if sorted(j)==s:
                        ans[proc].append(j)
        return list(ans.values())
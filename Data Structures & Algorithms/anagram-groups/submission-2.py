class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans:defaultdict=defaultdict(list)
        for word in strs:
            k="".join(sorted(word))
            ans[k].append(word)
        return list(ans.values())
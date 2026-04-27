class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ''    
        return ",".join([str(len(i)) for i in strs])+',#'+"".join(strs)
    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        print(s)
        size,res=[],[]
        i=s.index('#')
        size=s[:i].split(',')
        i+=1
        for j in size[:-1]:
            res.append(s[i:i+int(j)])
            i+=int(j)
        return res
        

        
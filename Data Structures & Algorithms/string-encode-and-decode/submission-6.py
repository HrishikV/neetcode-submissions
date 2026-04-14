class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ''    
        return ",".join([str(len(i)) for i in strs])+',#'+"".join(strs)
    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        print(s)
        size,res,i=[],[],0
        while s[i]!='#':
            cur=''
            while s[i]!=',':
                cur+=s[i]
                i+=1
            size.append(int(cur))
            i+=1
        i+=1
        for j in size:
            res.append(s[i:i+j])
            i+=j
        return res
        

        
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if len(t)> len(s) or t=='':
            return ''
        c,window={},{}
        for i in t:
            c[i]=c.get(i,0)+1
        have,need=0,len(c)
        res,reslen=[-1,-1],float('inf')
        l=0
        for r in range(len(s)):
            ch=s[r]
            window[ch]=window.get(ch,0)+1
            if ch in c and window[ch]==c[ch]:
                have+=1
            while have==need:
                if (r-l+1)<reslen:
                    res=[l,r+1]
                    reslen=r-l+1
                window[s[l]]-=1
                if s[l] in c and window[s[l]]<c[s[l]]:
                    have-=1
                l+=1

        try:
            return s[res[0]:res[1]]
        except:
            return ''
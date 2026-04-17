class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2!=0:
            return False
        start_p=['[','{','(']
        proc=[]
        pair={
                '}':'{',
                ']':'[',
                ')':'('     }
        for i in s:
            if i in start_p:
                proc.append(i)
            elif not proc:
                 return False
            elif pair[i]!=proc.pop():
                return False

        return len(proc)==0
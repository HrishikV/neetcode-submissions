class Solution:
    def isPalindrome(self, s: str) -> bool:
        k=""
        for i in s.lower():
            if i.isalnum():
                k+=i
        print(k)
        return k==k[::-1]
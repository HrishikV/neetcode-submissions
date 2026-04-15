class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        pos=(height[0],0)
        res=0
        inter=0
        for i in range(n):
            if i==0:
                continue
            elif pos[0]<=height[i]:
                res+=pos[0] *(i-pos[1]-1) - inter
                inter=0
                pos=(height[i],i)
            elif pos[0] >height[i] and height[i]==max(height[i:]):
                res+=height[i] *(i-pos[1]-1) - inter
                inter=0
                pos=(height[i],i)
            else:
                inter+=height[i]
        return res
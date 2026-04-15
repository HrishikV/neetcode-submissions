class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n=len(heights)
        area=0
        for i in range(n):
            for j in range(i+1,n):
                area=max(area,min(heights[i],heights[j])*(j-i))
        return area
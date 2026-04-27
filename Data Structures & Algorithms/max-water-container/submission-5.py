class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n=len(heights)
        area=0
        for i in range(n-1):
            for j in range(i+1,n):
                if heights[i] >heights[j]:
                    area=max(area,heights[j]*(j-i))
                else:
                    area=max(area,heights[i]*(j-i))
        return area
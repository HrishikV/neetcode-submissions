class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n=len(heights)
        area=set()
        for i in range(n-1):
            for j in range(i+1,n):
                if heights[i] >heights[j]:
                    area.add(heights[j]*(j-i))
                else:
                    area.add(heights[i]*(j-i))
        return max(area)
class MedianFinder:

    def __init__(self):
        self.nums=[]

    def addNum(self, num: int) -> None:
        self.nums.append(num)

    def findMedian(self) -> float:
        self.nums.sort()
        l=len(self.nums)

        if l%2==1:
            return self.nums[(l+1)//2 -1]/1
        else:
            return (self.nums[l//2] + self.nums[l//2 -1])/2
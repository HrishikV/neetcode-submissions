class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        nums=sorted(list(set(numbers)))
        for i in nums:
            s=target-i
            print(s,i)
            if s==i:
                continue
            
            if s in numbers:
                return [numbers.index(i)+1,numbers.index(s)+1]
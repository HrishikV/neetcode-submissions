class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        proc=set()
        for i in numbers:
            if i not in proc:
                proc.add(i)
                s=target-i
                print(s,i)
                if s==i:
                    continue
                
                if s in numbers:
                    return [numbers.index(i)+1,numbers.index(s)+1]
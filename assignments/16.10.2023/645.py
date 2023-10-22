class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums.sort()
        d = {}
        res = []

        for i in nums:
            d[i] = d.get(i,0)+1

        for i,value in d.items():
            if value > 1:
                res.append(i)

        for i in range(1,len(nums)+1):
            if i not in nums:
                res.append(i)        

        return res
                   
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        tot = 0
        for i in range(len(nums)):
            if i%2==0:
                tot+=nums[i]
        return tot        
            
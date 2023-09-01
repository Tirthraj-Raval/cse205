class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        newNums = []
        if(len(nums) == 1):
            return nums[0]%10
        else:
            for i in range(0, len(nums)-1):
                newNums.append(nums[i] + nums[i+1]%10) 
                nums[i] = newNums[i]
            nums.pop()   
            return self.triangularSum(nums)
                   

   
        
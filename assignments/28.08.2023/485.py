class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        arr = []
        for i in range(0, len(nums)):
            if(nums[i] == 1):
                count += 1

            elif(nums[i] != 1):
                arr.append(count)
                count = 0

            if(i == len(nums)-1):
                arr.append(count)
        return max(arr)    

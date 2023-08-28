class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        def backtrack(start, current_subset):
            result.append(list(current_subset))
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                current_subset.append(nums[i])
                backtrack(i + 1, current_subset)
                current_subset.pop()
                
        result = []
        nums.sort()  # Sorting the array to handle duplicates
        backtrack(0, [])
        return result
    
sol = Solution()
print(sol.subsetsWithDup([1, 2, 2]))
class Solution:
    
    def swap(self, arr, i, j):
        arr[i], arr[j] = arr[j], arr[i]
    
    def permute(self, nums: list[int]) -> list[list[int]]:
        def newPermute(index, arr, ans):
            if index == len(arr):
                ans.append(list(arr))
                return
            
            for i in range(index, len(arr)):
                self.swap(arr, index, i)
                newPermute(index + 1, arr, ans)
                self.swap(arr, index, i)
                
        ans = []
        newPermute(0, nums, ans)
        return ans class Solution:
    
    def swap(self, arr, i, j):
        arr[i], arr[j] = arr[j], arr[i]
    
    def permute(self, nums: list[int]) -> list[list[int]]:
        def newPermute(index, arr, ans):
            if index == len(arr):
                ans.append(list(arr))
                return
            
            for i in range(index, len(arr)):
                self.swap(arr, index, i)
                newPermute(index + 1, arr, ans)
                self.swap(arr, index, i)
                
        ans = []
        newPermute(0, nums, ans)
        return ans 
class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        def formCombinations(i, arr, target, ans, ds):
            if(i == len(arr)):
                if(target == 0):
                    ans.append(list(ds))
                return
            
            if(arr[i] <= target):
                ds.append(arr[i])
                formCombinations(i, arr, target - arr[i], ans, ds)
                ds.pop()
            formCombinations(i+1, arr, target, ans, ds) 
            
        ans = []
        ds = []
        formCombinations(0, candidates, target, ans, ds)
        return ans 
class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        def backtrack(i, arr, target, ans, ds):
            if(i == len(arr)):
                if(target == 0):
                    ans.append(list(ds))
                return
            if(arr[i] <= target):
                ds.append(arr[i])
                backtrack(i + 1, arr, target - arr[i], ans, ds)
                ds.pop()
            
                while i + 1 < len(arr) and arr[i + 1] == arr[i]:
                    i += 1
            
            backtrack(i + 1, arr, target, ans, ds)
            
        ans = []
        ds = []
        candidates.sort()  
        backtrack(0, candidates, target, ans, ds)
        return ans
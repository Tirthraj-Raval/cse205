class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        
        ans = []
        for x in arr2:
            while x in arr1:
                ans.append(x)
                arr1.remove(x)

        return ans+sorted(arr1)        

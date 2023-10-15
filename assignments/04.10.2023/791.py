class Solution:
    def customSortString(self, order: str, s: str) -> str:
        ans = ""
        for i in order:
            while i in s:
                ans = ans+i
                s = s.replace(i, "",1)
            
        ans+=s
        return ans            
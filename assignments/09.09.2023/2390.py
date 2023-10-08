class Solution:
    def removeStars(self, s: str) -> str:
        l1 = []
        for i in s:
            if i == "*":
                l1.pop()
            elif i =="*" and len(l1) == 0:
                continue
            else:
                l1.append(i)
        
        s1 = ""
        for i in l1:
            s1 = s1 + i
        
        return s1            
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        l1 = []
        l2 = []
        for i in s:
            if i== "#" and len(l1) !=0:
                l1.pop()
            elif i == "#" and len(l1) == 0:
                continue    
            else:
                l1.append(i)    
        for i in t:
            if i== "#" and len(l2)!=0:
                l2.pop()
            elif i =="#" and len(l2) == 0:
                continue    
            else:
                l2.append(i) 
                
        if len(l1) != len(l2):
            return False        

        for i in range(len(l1)):
            if l1[i] != l2[i]:
                return False 

        return True           
        
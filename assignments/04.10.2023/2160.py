class Solution:
    def minimumSum(self, num: int) -> int:
        l = []
        x = num
        for i in range(len(str(num))):
            a = num%10
            l.append(a)
            num //= 10
        
        l.sort()
        res = (l[1] * 10 + l[2]) + (l[0] * 10 + l[3])
        return res   
        
        
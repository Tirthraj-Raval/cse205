class Solution:
    def fib(self, number: int) -> int:
        if(number == 0):
           return 0
        elif(number == 1):
            return 1
        
        return self.fib(number - 1) + self.fib(number - 2)




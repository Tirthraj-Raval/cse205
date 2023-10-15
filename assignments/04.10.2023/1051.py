class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        temp = []
        temp+=heights
        print(temp)
        expected = []
        heights.sort()
        expected += heights
        
        count = 0
        for i in range(len(temp)):
            if temp[i] != expected[i]:
                count+=1

        return count        
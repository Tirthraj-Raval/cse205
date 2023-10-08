class Solution:
    def calPoints(self, operations: List[str]) -> int:
        list1=[]
        for i in operations:
            if i=="C":
                list1.pop()
            elif i=="D":
                list1.append(list1[-1]*2)
            elif i=="+":
                sm=list1[-2]+list1[-1]
                list1.append(sm)
            else:
                list1.append(int(i))

        return sum(list1)
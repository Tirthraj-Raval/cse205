class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        while len(stones) > 1:
            stones.sort()
            m1=max(stones)
            stones.remove(m1)
            m2=max(stones)
            stones.remove(m2)
        
            if m1 != m2:
                m2 = abs(m2 - m1)
                stones.append(m2)
        
        if len(stones) == 0:
            return 0
        return stones[0]
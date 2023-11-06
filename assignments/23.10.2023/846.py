class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        
        if len(hand)%groupSize != 0:
            return False
            
        n = len(hand)//groupSize
        total_count = 0
        hand.sort()

        while total_count != n:
            count = 0
            prev = hand[0]-1
            ind = 0
            while count != groupSize and ind <= len(hand) - 1:
                if prev == hand[ind] - 1:
                    prev = hand.pop(ind)
                    count+=1
                elif prev == hand[ind]:
                    ind+=1
                else:
                    return False    
            if count != groupSize:
                return False        
            total_count+=1 

        return True if len(hand) == 0 else False
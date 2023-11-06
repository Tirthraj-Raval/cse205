class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        result = []

        for i in nums:
            d[i] = d.get(i,0) + 1
        
        sorted_d = sorted(d.items(), key=lambda x:x[1], reverse=True)

        for num,freq in sorted_d[:k]:
            result.append(num)
        
        return result

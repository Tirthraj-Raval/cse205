class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        d = {}
        for i in nums:
            d[i] = d.get(i,0)+1
        sorted_items = sorted(d.items(), key=lambda x: x[0])  

        index = 0

        for color, count in sorted_items:
            for _ in range(count):
                nums[index] = color
                index += 1       
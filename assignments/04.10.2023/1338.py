class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        d = {}
        for i in arr:
            d[i] = d.get(i,0) + 1

        sorted_d = sorted(d.items(), key=lambda x : x[1], reverse = True)

        half_size = len(arr) // 2
        min_set_size = 0
        current_size = 0

        for key, freq in sorted_d:
            current_size += freq
            min_set_size += 1
            if current_size >= half_size:
                break

        return min_set_size
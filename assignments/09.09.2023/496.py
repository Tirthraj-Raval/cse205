class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        index = 0
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    index = j
                    break
                    
            for k in range(index, len(nums2)):
                if nums2[k] > nums1[i] :
                    ans.append(nums2[k])
                    break
                elif nums2[k]<=nums1[i] and k == len(nums2)-1:
                    ans.append(-1)        

        return ans                 
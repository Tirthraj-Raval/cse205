# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        curr2 = ListNode(0)
        dummy = curr2
        l1 = []
        while curr:
            l1.append(curr.val)
            curr = curr.next

        def merge_sort(arr):
            if len(arr) > 1:
                mid = len(arr) //2
                left_half = arr[:mid]
                right_half = arr[mid:]

                merge_sort(left_half)
                merge_sort(right_half) 

                i=j=k= 0
                while i < len(left_half) and j < len(right_half):
                    if left_half[i] < right_half[j]:
                        arr[k] = left_half[i]
                        i+=1
                    else:
                        arr[k] = right_half[j]
                        j+=1
                    k+=1

                while i < len(left_half):
                    arr[k] = left_half[i]
                    i+=1
                    k+=1
                while j< len(right_half):
                    arr[k] = right_half[j]
                    j+=1
                    k+=1

        merge_sort(l1)

        for i in l1:
            curr2.next = ListNode(i)
            curr2 = curr2.next

        return dummy.next        
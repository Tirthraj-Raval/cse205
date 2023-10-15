# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        count = 0
        dummy = ListNode(0)
        curr2 = dummy
        arr = []
        while curr:
            count+=1
            arr.append(curr.val)
            curr = curr.next

        def insertion_sort(arr):
            for i in range(1, len(arr)):
                key = arr[i]
                j = i - 1

                while j >= 0 and key < arr[j]:
                    arr[j + 1] = arr[j]
                    j -= 1

                arr[j + 1] = key      

        insertion_sort(arr)

        for i in arr:
            curr2.next = ListNode(i)
            curr2 = curr2.next

        return dummy.next    
        


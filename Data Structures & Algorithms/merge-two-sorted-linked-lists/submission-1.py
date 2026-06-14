# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)

        new_curr = dummy

        while list1 and list2:
            if list1.val < list2.val:
                new_curr.next = list1
                new_curr = new_curr.next
                list1 = list1.next

            else:
                new_curr.next = list2
                new_curr = new_curr.next
                list2 = list2.next
        
        if list1:
            new_curr.next = list1

        if list2:
            new_curr.next = list2
        return dummy.next
        
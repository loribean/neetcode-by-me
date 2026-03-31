# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        new_current = dummy

        while list1 and list2:
            if list1.val < list2.val:
                new_current.next = list1
                list1 = list1.next
            else:
                new_current.next = list2
                list2 = list2.next
            new_current = new_current.next

        if list1:
            new_current.next = list1
        elif list2:
            new_current.next = list2

        return dummy.next
        
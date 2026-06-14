# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        #Fast & slow pointers: Split the list in half
        #Reverse linked list: Change direction of second half
        #Merge two lists: Interleave nodes

        if not head or not head.next:
            return
        #1) find the middle using fast and slow pointer

        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        #2 Reverse the second half of the list
        prev = None
        curr = slow.next
        slow.next = None #terminate the first list

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        #3 Merge the arrays

        first, second = head, prev

        while second:
            next1, next2 = first.next, second.next
            first.next = second
            second.next = next1

            first = next1
            second = next2




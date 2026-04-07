# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    #we can solve this w min heap also
    #but lets solve using iteration
    #naive approach is to merge the lists, sort them, and create the linkedlist
    #but that is O(n*k)
    # we can do a divide and conquer
    # since we split into sub problems of two, it will be 0(nlogk)
    # where k is no of lists and n is number of nodes
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        #edge case, return if lists is empty or null
        if len(lists) == 0 or not lists:
            return None
    

        # we merge the lists till lists is 1 in length
        while len(lists) > 1:
            #local var to store merged lists
            mergedLists = []
            
            #we recursively merge the lists in twos
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                mergedLists.append(self.mergeLists(l1, l2))
            #then replace lists with mergedLists
            lists = mergedLists
        return lists[0]

    #same as merge 2 sorted lists
    def mergeLists(self, l1, l2):
        #initialize to a dummy node first to handle null case
        dummy = ListNode()
        current = dummy
        while l1 and l2: # while both l1 and l2 exist
            if l1.val < l2.val: # l1 is smaller than l2, we put l1 first
                current.next = l1
                l1 = l1.next
            else: # l2 is smaller than l1, we put l2 first
                current.next = l2
                l2 = l2.next
            current = current.next # move to the next

        #exited the while loop, meaning one list became none
        if l1 is not None: # l1 still exists, and is still sorted, we can just slap it at the back
            current.next = l1
        if l2 is not None:
            current.next = l2 #same

        return dummy.next #return the dummy.next

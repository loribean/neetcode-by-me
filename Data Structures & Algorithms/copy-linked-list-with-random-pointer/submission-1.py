"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        if not head:
            return None
            
        nodes = {}
        current = head
        while current:
            copy = Node(current.val)
            nodes[current] = copy
            current = current.next

        current = head
        while current:
            copy = nodes[current]
            copy.next = nodes.get(current.next, None)
            copy.random = nodes.get(current.random, None)
            current = current.next
        
        return nodes[head]
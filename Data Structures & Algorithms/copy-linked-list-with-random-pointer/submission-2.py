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

        nodes = collections.defaultdict(lambda: Node(0))
        nodes[None] = None
        current = head
        while current:
            nodes[current].val = current.val
            nodes[current].next = nodes[current.next]
            nodes[current].random = nodes[current.random]
            current = current.next
        current = head
        
        return nodes[head]
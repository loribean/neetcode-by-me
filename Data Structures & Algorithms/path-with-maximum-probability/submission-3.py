class Solution:
    def maxProbability(
        self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int
    ) -> float:

        # this is a shortest path between start and end
        # where the edges are weighted

        # lets first form the adj list

        adj = {}

        for i in range(n+1):
            adj[i] = []

        lenSuccProb = len(succProb)

        for i in range(len(edges)):
            src, dest = edges[i]
            if i < len(succProb):
                weight = succProb[i]
            else:
                weight = 0

            adj[src].append((dest, weight))
            adj[dest].append((src, weight))

        shortest = {}
        # the heart of djikstra, the min heap, where we usually pop the min weigh
        # for this problem though, we want to pop the max
        maxHeap = [(-1.0, start_node)]

        while maxHeap:
            w1, n1 = heapq.heappop(maxHeap)
            w1 = -w1

            if n1 in shortest:
                continue
            shortest[n1] = w1

            if n1 == end_node:
                return w1

            for n2, w2 in adj[n1]:
                if n2 not in shortest:
                    heapq.heappush(maxHeap, (-(w1 * w2), n2))

        return 0.0
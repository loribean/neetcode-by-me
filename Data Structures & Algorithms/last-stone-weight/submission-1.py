class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        stone_neg = [-1 * stone for stone in stones]

        heapq.heapify(stone_neg)

        while len(stone_neg) > 1:
            x = heapq.heappop(stone_neg)
            y = heapq.heappop(stone_neg)

            if x == y:
                continue
            else:
                heapq.heappush(stone_neg,x-y)

        if len(stone_neg) == 0:
            return 0

        return -1 * stone_neg[0]
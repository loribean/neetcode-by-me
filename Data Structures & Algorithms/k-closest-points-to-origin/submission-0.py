class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        arr = []
        heapq.heapify(arr)

        for x,y in points:
            res = x**2 + y**2

            heapq.heappush(arr,(-res, [x, y]))
            if len(arr) > k:
                heapq.heappop(arr)

        return [heapq.heappop(arr)[1] for _ in range(k)]
        
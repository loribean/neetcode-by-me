class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        new = []
        heapq.heapify(new)
        
        for item in nums:
            heapq.heappush(new,item)
            if len(new) > k:
                heapq.heappop(new)
        
        return new[0]
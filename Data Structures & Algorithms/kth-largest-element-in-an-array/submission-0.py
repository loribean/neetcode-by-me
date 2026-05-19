class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        heapq.heapify(nums)
        res = 0
        number = len(nums) - k + 1
        
        while number > 0:
            res = heapq.heappop(nums)
            number -= 1
        
        return res
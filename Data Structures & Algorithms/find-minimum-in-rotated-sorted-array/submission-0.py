class Solution:
    def findMin(self, nums: List[int]) -> int:
        #rotating an array means that we shift the back element to the front.
        #Since we need to do a O(logn) solution, lets do binary search

        l, r = 0, len(nums) -1
        res = float("infinity")

        while l <= r:

            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break

            m = (l+r) //2
            res = min(res, nums[m])

            if nums[m] >= nums[l]: # we are in the left sorted portion, so we want to search the right
                l = m + 1
            else:
                r = m - 1 # we are in the right sorted position, so we want to search the right
        return res
            
        
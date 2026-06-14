class Solution:
    def search(self, nums: List[int], target: int) -> int:

        min_index = self.findMin(nums)
        #find selected half that the target lives
        if nums[min_index] <= target and target <= nums[-1]:
            #we perform binary search on the second half of the array
            return self.binarySearch(nums, target, min_index, len(nums)-1)
        else:
            #we perform binary search on the first half of the array
            return self.binarySearch(nums,target, 0, min_index-1)

    def binarySearch(self,nums: List[int], target: int, l: int, r: int) -> int:
        while l <= r:
            mid = (l+r)//2
            val = nums[mid]
            if val > target:
                r = mid -1
            elif val < target:
                l = mid + 1
            else:
                return mid
        return -1

    def findMin(self, nums: List[int]) -> int:
            l, r = 0, len(nums) - 1
            while l < r:
                m = l + (r - l) // 2
                if nums[m] < nums[r]:
                    r = m
                else:
                    l = m + 1
            return l


            
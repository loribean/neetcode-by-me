class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
            if not nums: return 0
            k = 1  # Pointer for the next unique element
            for i in range(1, len(nums)): #start iterating from 1 as the 0th index is always unique
                if nums[i] != nums[i-1]: #if nums[1] is not equal to nums[0], we found a unique item, so, write nums[k] as this unique value, if there was no such value, nth will be written aka skipped!
                    nums[k] = nums[i]
                    k += 1

            return k
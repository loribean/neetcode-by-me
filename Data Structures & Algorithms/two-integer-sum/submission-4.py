class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        sums = {}

        for i in range(len(nums)):
            sums[nums[i]] = i


        for i,num in enumerate(nums):
            complement = target - num
            if complement in sums and sums[complement] != i:
                return [i, sums[complement]]

        return []
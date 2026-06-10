class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        sum_dict = {}
        res = []

        for i in range(len(nums)):
            sum_dict[nums[i]] = i

        
        for i, num in enumerate(nums):
            complement = target - num
            if complement in sum_dict and sum_dict[complement] != i:
                return [i, sum_dict[complement]]

        return []


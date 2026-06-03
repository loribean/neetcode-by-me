class Solution:
    def rob(self, nums: List[int]) -> int:
        #bottom up dp

        prev_max = 0
        current_max = 0

        for i in range(len(nums)):
            # at any one house, the max money you can have is:
            # 1. max money from the prev house (skipping house i)
            # 2. or money in house i + max money from two houses ago

            #figure out which is bigger, prev_max + nums[i] OR current_max (num[i-1])
            new_max = max(prev_max + nums[i], current_max)
            prev_max = current_max
            current_max = new_max

        return current_max


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums:
            return 0

        numSet = set(nums)
        longest = 1

        for num in numSet:
            if (num -1) not in numSet:
                #we found our start of sequence
                length = 1
                while (length + num) in numSet:
                    length += 1
                longest = max(longest, length)
        
        return longest
        
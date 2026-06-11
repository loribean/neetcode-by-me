class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        #for 3 sum, its kinda similar to a 2 sum
        # in a sense that we need to look for a complement
        # except that the complement would be 2 numbers that add up to be neg of the 1st

        # so, lets sort the array first

        res = []
        nums.sort() #O(nlogn) + On^2

        for i in range(len(nums)):

            first = nums[i]
            # If the current number is greater than 0, 3 positive numbers can't sum to 0
            if first > 0:
                break
                
            if i > 0 and first == nums[i-1]:
                continue

            #lets do two pointers to find the sum of numbers that equal to the negative of first

            l = i+1
            r = len(nums)-1

            while l < r:
                threeSum = first + nums[l] + nums[r]

                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([first, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1

        return res


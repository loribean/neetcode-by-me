class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #use bucket sort

        my_dict = {}
        frequency = [[] for i in range(len(nums)+1)]

        for num in nums:
            my_dict[num] = my_dict.get(num,0)  +1

        for num,count in my_dict.items():
            frequency[count].append(num)

        res = []

        for i in range(len(frequency) -1,-1,-1):
            for num in frequency[i]:
                res.append(num)
                if len(res)==k:
                    return res

        



        
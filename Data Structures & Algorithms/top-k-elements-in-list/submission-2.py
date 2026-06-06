class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #use bucket sort
        #initialize an array
        my_dict = {}
        #initialise a frequency array, where in each item will be a empty array
        frequency = [[] for i in range(len(nums)+1)]

        #iterate through nums to build the dictonary for ez lookup, how many times was a word used
        for num in nums:
            my_dict[num] = my_dict.get(num,0)+1

        #iterate through the dict to build the frequency array
        for num,count in my_dict.items():
            frequency[count].append(num)

        res = []

        #loop backwards through the frequency array
        for i in range(len(frequency) -1,-1,-1):
            for num in frequency[i]:
                res.append(num)
                #each time we add to res, we check if res is k length
                if len(res)==k:
                    return res

        #time complexity is O(n+k) where k could worse case be == n, which means that it could be O(2n), but we drop the coeefficient

        



        
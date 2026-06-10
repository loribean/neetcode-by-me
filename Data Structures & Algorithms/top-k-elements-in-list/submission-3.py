class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        #we can probably sort it
        #that would be at least n log n
        #or we could do bucket sort, which would be n? or 2 n

        lookup = collections.defaultdict(int)
        frequency = [[] for i in range(len(nums)+1)]

        res = []

        #create the lookup
        for num in nums:
            lookup[num] += 1

        #populate the frequency
        for num, count in lookup.items():
            frequency[count].append(num)
        
        for i in range(len(frequency) -1, -1, -1):
            for num in frequency[i]:
                res.append(num)
                if len(res) == k:
                    return res

            



        
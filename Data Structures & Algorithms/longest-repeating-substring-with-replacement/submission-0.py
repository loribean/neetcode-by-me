class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #sliding window 
        # 2 pointer
        # create a hashmap of all the alphabets
        
        count = collections.defaultdict(int)
        res = 0

        #initialize a l and r pointer
        l = 0

        for r in range(len(s)):
            count[s[r]] += 1

            while r - l + 1 - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r-l+1)

        return res



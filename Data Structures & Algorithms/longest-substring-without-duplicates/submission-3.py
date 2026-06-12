class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #sliding window
        if not s:
            return 0
        # 2 pointers
        l, r = 0,1
        max_length = 1
        my_set = set()
        my_set.add(s[l])

        for r in range(1,len(s)):
            while s[r] in my_set:
                my_set.remove(s[l])
                l += 1
            current_length = r - l + 1
            max_length = max(current_length,max_length)
            my_set.add(s[r])
        return max_length
        



        
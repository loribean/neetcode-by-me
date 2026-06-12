class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #SLIDING WINDOW will be the size of s1
        #L & R pointer

        #loop through s2 with window size s1 to see if a variation of s1 occurs

        #but first, we check if s1 > s2. 
        if len(s1) > len(s2):
            return False

        l = 0
        r = len(s1) -1
        

        s1_map = collections.defaultdict(int)
        s2_map = collections.defaultdict(int)
        for i in range(len(s1)):
            s1_map[s1[i]] += 1

    
        for r in range(len(s2)):
            s2_map[s2[r]] += 1
            # If the window size exceeds len(s1), shrink it from the left
            if (r - l + 1) > len(s1):
                s2_map[s2[l]] -= 1
                if s2_map[s2[l]] == 0:
                    del s2_map[s2[l]] # Crucial for dict comparison!
                l += 1
            if s1_map == s2_map:
                return True
        return False

        
        
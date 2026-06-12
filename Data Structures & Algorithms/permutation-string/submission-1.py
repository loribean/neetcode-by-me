class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #SLIDING WINDOW will be the size of s1
        #L & R pointer

        #loop through s2 with window size s1 to see if a variation of s1 occurs

        #but first, we check if s1 > s2. 
        if len(s1) > len(s2):
            return False

        l = 0
        r = len(s1)

        while r < len(s2) +1:
            if sorted(s1) == sorted(s2[l:r]):
                return True
            else:
                l += 1
                r += 1
        return False

        
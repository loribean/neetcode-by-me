class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(s) < len(t) or t == "":
            return ""

        countT, window = {}, {}

        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        have, need = 0, len(countT) #unique chars in T
        l = 0
        res, resLen = [-1,-1], float("infinity")
        
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            if c in countT and window[c] == countT[c]:
                have += 1

            while have == need: #we satisfied our window
                #update our res
                if (r -l + 1) < resLen:
                    res = [l,r]
                    resLen = (r-l +1)
                #lets pop from left of the window, see if we can make it shorter
                window[s[l]] -= 1
                #did we just dis-satistifed our end condition?
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1

        l, r = res

        if resLen != float("infinity"):
            return s[l:r+1]
        else:
            return ""




    
            
            


        
        
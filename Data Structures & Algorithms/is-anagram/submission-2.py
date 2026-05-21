class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        s_lookup, t_lookup = {}, {}

        for i in range(len(s)):
            s_lookup[s[i]] = 1 + s_lookup.get(s[i],0)
            t_lookup[t[i]] = 1 + t_lookup.get(t[i],0)
        return t_lookup == s_lookup
            
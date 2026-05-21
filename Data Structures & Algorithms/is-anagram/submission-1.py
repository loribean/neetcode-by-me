class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        s_lookup = {}

        for letter in s:
            if letter not in s_lookup:
                s_lookup[letter] = 1
            else:
                s_lookup[letter] += 1

        t_lookup = {}

        for letter in t:
            if letter not in s_lookup:
                return False
            if letter not in t_lookup:
                t_lookup[letter] = 1
            else:
                s_val = s_lookup[letter]
                t_lookup[letter] += 1
                if s_val < t_lookup[letter]:
                    return False
        
        for letter in t_lookup.keys():
            if t_lookup[letter] != s_lookup[letter]:
                return False
        if len(t_lookup.keys()) != len(s_lookup.keys()):
            return False
        return True
            
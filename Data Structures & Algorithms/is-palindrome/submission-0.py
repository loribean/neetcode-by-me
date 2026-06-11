class Solution:
    def isPalindrome(self, s: str) -> bool:
        #lets have two pointers, one from start and one from end of string
        cleaned = "".join(char for char in s if char.isalnum())
        i = 0
        j = len(cleaned) - 1


        while i < j:
            start = cleaned[i]
            end = cleaned[j]

            if start.lower() == end.lower():
                i += 1
                j -= 1
                continue
            else:
                return False
        
        return True

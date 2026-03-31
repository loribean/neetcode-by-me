class Solution:
    def isValid(self, s: str) -> bool:
        #iterate through the string
        #if its an opening bracket type, if yes then store in a stack
        #if not then pop from the stack to see if matching

        if len(s) < 2:
            return False

        stack = []
        for letter in s:
            match letter:
                case "("| "[" |"{":
                    stack.append(letter)
                case ")":
                    if len(stack) == 0 or stack.pop() != "(":
                        return False
                case "]":
                    if len(stack) == 0 or stack.pop() != "[":
                        return False
                case "}":
                    if len(stack) == 0 or stack.pop() != "{":
                        return False

        if len(stack) == 0:
            return True
        else:
            return False
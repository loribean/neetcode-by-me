class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #use a stack to store the numbers

        stack = []

        for token in tokens:
            if token not in "+-*/":
                stack.append(int(token))
            #append to stack till we hit a operand, then
            # pop from the stack to calculate and 
            #append the result to the stack again
            else:
                one = stack.pop()
                two = stack.pop()

                if token == "+":
                    res = one + two
                elif token == "-":
                    res = two - one
                elif token == "*":
                    res = one * two
                elif token == "/":
                    res = int(two / one)
                stack.append(res)

        return stack[-1]

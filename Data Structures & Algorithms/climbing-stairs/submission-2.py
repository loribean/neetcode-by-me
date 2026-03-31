class Solution:
    def climbStairs(self, n: int) -> int:
        # Base cases: if there are 1 or 2 steps, 
        # the answer is just n itself.
        if n <= 2:
            return n
        # We start tracking from step 1 and step 2
        # 'one_back' is the ways to reach the step immediately behind us
        # 'two_back' is the ways to reach the step two behind us
        one_back = 2
        two_back = 1

        for i in range(3, n+1):
            # We start our loop from the 3rd step up to n
            # The ways to reach the CURRENT step is the sum of the last two
            current = one_back + two_back
            # Now, move our pointers forward for the next step in the loop
            two_back = one_back
            one_back = current
            
        return one_back

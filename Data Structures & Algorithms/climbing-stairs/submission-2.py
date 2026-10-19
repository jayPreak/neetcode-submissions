class Solution:
    mapi = {1: 1}
    def climbStairs(self, n: int) -> int:

        p = 1
        q = 1

        for i in range(n-1):
            temp = p
            p = p + q
            q = temp

        return p

        
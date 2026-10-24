class Solution:
    def isHappy(self, n: int) -> bool:
        setI = {}
        def sumOfA(n):
            total = 0
            ss = str(n)
            # for i in range(len(n))
            for c in ss:
                total += int(c) ** 2
            print("total is", total)
            return total

        
        while True:
            s = sumOfA(n)
            print("s", s)
            if s == 1:
                return True
            print("the set", setI)
            if s in setI:
                return False
            else:
                setI[s] = 1

            n = s






             
        
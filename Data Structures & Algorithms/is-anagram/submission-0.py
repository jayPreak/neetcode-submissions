class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dictS = {}
        dictT = {}

        if len(s) != len(t):
            return False
        else:
            for i in range(len(s)):
                if s[i] in dictS:
                    dictS[s[i]] += 1
                else:
                    # print(s[i])
                    dictS[s[i]] = 1
                    # print(dictS)

                if t[i] in dictT:
                    dictT[t[i]] += 1
                else:
                    # print(s[i])
                    dictT[t[i]] = 1
        if dictS == dictT:
            return True
        return False
        
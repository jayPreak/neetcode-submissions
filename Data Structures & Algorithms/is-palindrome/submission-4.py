import string

class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 1:
            return True
        allowed = list(string.ascii_letters + string.digits)

        # print(allowed)
        s = s.lower()
        s = s.replace(" ", "")
        print(s)
        i = 0
        j = len(s)-1
        # endOfJ = -len(s)

        while i < j:
            print("i char", s[i])
            print("j char", s[j])
            if s[i] not in allowed:
                i+=1
                continue
            if s[j] not in allowed:
                j-=1
                continue

            if s[i] == s[j]:
                i+=1
                j-=1
            else:
                return False

        # while i < len(s):
            # print("i", i)
            # if s[i] not in allowed:
            #     i+=1
            
            # while j>-1:
            #     print("j", j)
                

            #     print("i", i)
            #     if i > len(s)-1:
            #         return True

                
                
            #     if i>j:
            #         break
        return True
                
                
        
        
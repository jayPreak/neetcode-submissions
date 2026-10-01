class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for i in strs:
            encoded += chr(len(i)) + i

        return encoded
    def decode(self, s: str) -> List[str]:
        print(s)
        res = []
        
        # print(ord(s[0]))
        while s:
            size = ord(s[0])
            word = s[1:size+1]
            res.append(word)
            s = s[size+1:]
        # print(s)
        # if s == "0#":
        #     return [""]

        # if len(s) == 3:
        #     return [str(s[2])]
        # lenC = int(s[0])
        # res = []
        # i =2

        # while i < len(s):
            
        #     if s[i] != "#":
        #         res.append(s[i: i+lenC])
        #     i += lenC+2
        #     if lenC + 3 > len(s):
        #         break
        #     lenC = int(s[lenC+2])
            
            # print(lenC)

        # print(res)

        return res
        


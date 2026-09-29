class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]
        res = {}

        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c) - ord("a")] += 1

            if tuple(count) not in res:
                res[tuple(count)] = [s]
            else:
                res[tuple(count)].append(s)

        # print(res.values())


        




        # print(res)

        return list(res.values())


        
        
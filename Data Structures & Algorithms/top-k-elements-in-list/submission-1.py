class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        resDict = {}
        resList = [[] for _ in range(len(nums)+1) ]
        actualRes = []

        for i in nums:
            if i not in resDict:
                resDict[i] = 1
            else:
                resDict[i] += 1
        
        # highest = resDict[nums[0]]
        # print(highest)

        for key, value in resDict.items():
            resList[value].append(key)
        for i in range(len(nums), 0, -1):
            for n in resList[i]:
                actualRes.append(n)
                if len(actualRes) == k:
                    return actualRes

        print(resList)
        return resList
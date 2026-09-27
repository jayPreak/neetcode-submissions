class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hasSeen = set()
        for i in nums:
            # print(i)
            # print('meow')
            # print(hasSeen)
            if i in hasSeen:
                return True
            hasSeen.add(i)
        
        return False
        
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for x in range(len(nums)):
            for y in range(1, len(nums)):
                # print(x, "x is ")
                # print(nums[x])
                # print("meow")
                # print(nums[y])
                if (x != y) and (nums[x] + nums[y]) == target:
                    return [x, y]

        return False

        
        
        
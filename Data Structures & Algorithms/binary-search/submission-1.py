class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1
        # print(l, r)

        
        # print(mid)
        while l<=r:
            isEven = (l+r+1) % 2 == 0
            print("iseen", isEven)
            if isEven:
                mid = int((l+r+1) / 2)
                # mid = int((r-l+1) / 2)
            else:
                mid = int((l+r) / 2)
                

            print(l, r, mid)
            if nums[mid] == target:
                return mid
            
            if nums[mid] < target:
                l = mid+1
            else:
                r = mid-1

        return -1

        
        
        
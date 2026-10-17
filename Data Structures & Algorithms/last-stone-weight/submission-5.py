class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-x for x in stones]
        heapq.heapify(maxHeap)

        while len(maxHeap) > 1:
            
            print("before", maxHeap)
            first = heapq.heappop(maxHeap)
            second = heapq.heappop(maxHeap)
            print("first", first)
            print("second", second)

            if second > first:
                heapq.heappush(maxHeap, first - second)

            print(maxHeap)

        return abs(maxHeap[0]) if len(maxHeap) > 0 else 0
                
        
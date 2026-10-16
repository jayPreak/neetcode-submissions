class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap = nums
        self.k = k

        heapq.heapify(self.minHeap)
        print("efore", self.minHeap)
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)
        print("after", self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        print("in add", self.minHeap)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)

        return self.minHeap[0]
        

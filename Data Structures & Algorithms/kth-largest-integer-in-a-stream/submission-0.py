class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.minH = []
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        if len(self.minH) < self.k:
            heapq.heappush(self.minH, val)
        elif val > self.minH[0]:
            heapq.heappop(self.minH)
            heapq.heappush(self.minH, val)
        
        return self.minH[0]
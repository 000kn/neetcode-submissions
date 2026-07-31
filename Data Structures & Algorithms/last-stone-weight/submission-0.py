

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stonespq = [-i for i in stones]
        heapq.heapify(stonespq)

        while len(stonespq) > 1:
            first = -heapq.heappop(stonespq)
            second = -heapq.heappop(stonespq)
            diff = first - second

            if diff > 0:
                heapq.heappush(stonespq, -diff)

        if stonespq:
            return -stonespq[0]
        else:
            return 0
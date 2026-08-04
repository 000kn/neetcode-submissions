class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)      #hashmap
        maxH = [-v for v in count.values()]
        heapq.heapify(maxH)

        time = 0
        q = deque()

        while maxH or q:
            time += 1

            if maxH:
                cnt = 1 + heapq.heappop(maxH)
                if cnt:
                    q.append([cnt, time + n])
            if q and q[0][1] == time:
                heapq.heappush(maxH, q.popleft()[0])

        return time
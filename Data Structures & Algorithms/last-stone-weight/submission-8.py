import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = []
        for stone in stones:
            maxHeap.append(-stone)
        heapq.heapify(maxHeap)
        while len(maxHeap) > 1:
            st1 = heapq.heappop(maxHeap)
            st2 = heapq.heappop(maxHeap)
            res= abs( st1 - st2)
            if res != 0:
                heapq.heappush(maxHeap,-res)
        return 0 if len(maxHeap) == 0 else -maxHeap[0]
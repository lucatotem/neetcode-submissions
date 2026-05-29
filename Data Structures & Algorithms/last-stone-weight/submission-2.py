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
        if len(maxHeap) == 0:
            return 0
        else:
            return -maxHeap[0]
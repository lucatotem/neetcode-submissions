import heapq
import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []
        for i,point in enumerate(points):
            heapq.heappush(maxHeap,[-math.sqrt((point[0] - 0)**2 + (point[1] - 0)**2),i])
            if len(maxHeap) > k:
                heapq.heappop(maxHeap)
        res = [points[maxHeap[i][1]] for i in range(len(maxHeap))]
        return res
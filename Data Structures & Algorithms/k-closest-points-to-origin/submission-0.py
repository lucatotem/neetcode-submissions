import heapq
import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []
        for i,point in enumerate(points):
            maxHeap.append([-math.sqrt((point[0] - 0)**2 + (point[1] - 0)**2),i])
        heapq.heapify(maxHeap)
        print(maxHeap)
        while len(maxHeap) > k:
            heapq.heappop(maxHeap)
        print(maxHeap)
        res = [points[maxHeap[i][1]] for i in range(len(maxHeap))]
        return res
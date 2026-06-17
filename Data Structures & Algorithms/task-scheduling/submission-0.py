from collections import Counter,deque
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        frequencyList = list(Counter(tasks).values())
        dq = deque([])

        heapq.heapify_max(frequencyList)
        time = 0
        while frequencyList or dq:
            print(dq)
            print(frequencyList)
            print(time)
            if dq and dq[0][1] == time:
                temp_val,temp_time = dq.popleft()
                heapq.heappush_max(frequencyList,temp_val)
            if frequencyList:
                temp = heapq.heappop_max(frequencyList)
                if temp != 1:
                    dq.append((temp-1,time+n+1))
            time+=1
        return time

            
                
from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for num in nums]
        dic = defaultdict(int)
        for num in nums:
            dic[num] += 1
        for num in dic:
            buckets[dic[num]-1].append(num)
        res = []
        for bucket in reversed(buckets):
            for item in bucket:
                if k == 1:
                    res.append(item)
                    return res
                res.append(item)
                k = k-1

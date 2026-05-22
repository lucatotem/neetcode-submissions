class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        currentLongest = 0
        l = h = 0
        current = 0
        currentset= set()
        while h<len(s):
            if s[h] not in currentset:
                current += 1
                currentset.add(s[h])
                h+=1
            else:
                currentLongest = max(h-l,currentLongest)
                currentset.remove(s[l])
                l+=1
        return max(h-l,currentLongest) 
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^a-z0-9]','',s.lower())

        a, b = 0, len(s)-1
        while a < b:
            if s[a] != s[b]:
                return False
            a = a + 1
            b = b - 1
        return True

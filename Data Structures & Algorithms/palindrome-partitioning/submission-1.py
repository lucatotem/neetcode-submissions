class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        cur = []
        def isPali(string):
            l,r = 0,len(string)-1
            while l<r:
                if string[l] != string[r]:
                    return False
                l+=1
                r-=1
            return True

        def dfs(i):
            if i == len(s):
                res.append(cur[::])
                return
            for j in range(i+1,len(s)+1):
                print(i)
                print(s[i:j])
                if isPali(s[i:j]):
                    cur.append(s[i:j])
                    dfs(j)
                    cur.pop()
        dfs(0)
        return res
        
                
        
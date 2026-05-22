class Solution:
    def isValid(self, s: str) -> bool:
        parmap = {'{' : '}', '[': ']', '(': ')'}
        stack = []
        for ch in s:
            if ch in parmap:
                stack.append(ch)
            else:
                print(stack)
                if len(stack)>0 and ch == parmap[stack[-1]]:
                    stack.pop()
                else:
                    return False
        if len(stack)>0:
            return False
        return True
                    

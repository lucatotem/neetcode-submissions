class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone_map = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }
        res = []
        cur = []
        def dfs():
            if len(cur) == len(digits):
                if len(cur)>0:
                    res.append("".join(cur))
                return
            for l in phone_map[digits[len(cur)]]:
                cur.append(l)
                dfs()
                cur.pop()
        dfs()
        return res
class Solution:

    def encode(self, strs: List[str]) -> str:
        chunks = []
        for s in strs:
            chunks.append(f"{len(s)}#{s}")
        return "".join(chunks)
    def decode(self, s: str) -> List[str]:
        a = 0
        res= []
        while a < len(s):
            b = s.find('#',a)

            l = int(s[a:b])

            res.append(s[b+1:b+1+l])

            a = b+1+l
        return res

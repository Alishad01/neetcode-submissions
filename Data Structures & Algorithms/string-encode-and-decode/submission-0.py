class Solution:
    def encode(self, strs: List[str]) -> str:
        code = ""
        for s in strs:
            code += str(len(s)) + '#' + s
        return code
    def decode(self, s: str) -> List[str]:
        i = 0
        res= []
        while i < len(s):
            j = i
            while s[j] != '#':
                j+=1
            
            length = int(s[i:j])
            res.append(s[j+1: j+1+length])

            i=j+1+length
        return res
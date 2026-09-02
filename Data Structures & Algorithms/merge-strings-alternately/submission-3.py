class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n = len(word1) if len(word1) > len(word2) else len(word2)
        i = 0
        s=""
        while i <= n:
            if i < len(word1):
                s+=word1[i]
            if i < len(word2):
                s+=word2[i]
            i+=1
        return s
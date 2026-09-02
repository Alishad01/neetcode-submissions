class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        s=""
        if len(word1) > len(word2):
            while i < len(word2):
                s+=word1[i]
                s+=word2[i]
                i+=1
            s+=word1[i:]
        elif len(word1) < len(word2):
            while i < len(word1):
                s+=word1[i]
                s+=word2[i]
                i+=1
            s+=word2[i:]
        else:
            for i in range(len(word1)):
                s+=word1[i]
                s+=word2[i]
        return s
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashy={}
        hashyy={}
        for i in s:
            if i not in hashy:
                hashy[i]=0
            else:
                hashy[i]+=1
        for j in t:
            if j not in hashyy:
                hashyy[j]=0
            else:
                hashyy[j]+=1
        return hashy==hashyy
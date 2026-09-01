class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        if len(strs)==0:
            return []
        for st in strs:
            characters = [0] * 26
            for i in st:
                characters[ord(i) - ord('a')] +=1
            res[tuple(characters)].append(st)
        return list(res.values())
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        memo={}
        for i in nums:
            if i not in memo:
                memo[i]=1
            else:
                memo[i]+=1
        memo=sorted(memo, key=lambda x: memo[x], reverse=True)
        val = [memo[i] for i in range(k)]
        return val
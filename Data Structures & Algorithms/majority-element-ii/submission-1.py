class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        arr=[]
        hashy={}
        for i in nums:
            if i in hashy:
                hashy[i]+=1
                
            else:
                hashy[i]=0
            if hashy[i] >= n//3 and i not in arr:
                arr.append(i)
        return arr
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_count = 1
        count = 1
         
        if len(nums)==0:
            return 0
        
        arr = sorted(nums)

        for i in range(len(arr)-1):
            if arr[i]+1 == arr[i+1]:
                count+=1

            elif arr[i]==arr[i+1]:
                pass

            else:
                count = 1

            max_count = max(max_count, count)

        return max_count
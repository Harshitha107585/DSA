class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        total = sum(nums)
        left = 0
        curr = 0
        maxlen = -1

        target = total - x
        for right in range(len(nums)):
            curr+=nums[right]

            while curr > target and left <= right:
                curr-=nums[left]
                left+=1
            if curr == target:
                maxlen =max(maxlen,right-left+1)
        if maxlen == -1:
            return -1
        return len(nums) - maxlen          
                


    

            
            
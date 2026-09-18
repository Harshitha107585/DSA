class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float("-inf")
        sum = 0
        for num in nums:
            sum+=num

            if sum > max_sum:
                max_sum = sum
            if sum < 0:
                sum = 0 

        return max_sum        
                




        
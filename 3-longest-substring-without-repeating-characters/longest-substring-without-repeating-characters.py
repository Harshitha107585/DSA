class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dict1 = {}
        left = 0 
        ans = 0
        for right in range(len(s)):
            if s[right] in dict1 and dict1[s[right]] >= left:
                left = dict1[s[right]]+1
            dict1[s[right]] = right
            ans = max(ans,right-left+1)
        return ans        


        
           
             

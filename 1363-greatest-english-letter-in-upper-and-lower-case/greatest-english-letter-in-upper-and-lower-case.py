class Solution:
    def greatestLetter(self, s: str) -> str:
        ans = ""
        for ch in set(s):
            if ch.islower() and ch.upper() in s:
                ans = max(ans,ch.upper())
        return ans        
        
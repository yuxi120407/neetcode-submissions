class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        current_window = set()
        l = 0
        best = 0
        for r in range(len(s)):
            while s[r] in current_window:
                current_window.remove(s[l])
                l+=1
            current_window.add(s[r])
            best = max(best, r-l+1)
        return best






        
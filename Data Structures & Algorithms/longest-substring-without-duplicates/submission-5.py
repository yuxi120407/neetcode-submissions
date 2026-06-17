class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        
        for i in range(len(s)):
            current_len = set() 
            for j in range(i, len(s)):
                if s[j] in current_len:
                    break
                current_len.add(s[j])
            max_len = max(len(current_len), max_len)
        return max_len



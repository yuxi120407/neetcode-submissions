class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        best = 0
        for i in range(len(s)):
            current_s = set()
            for j in range(i, len(s)):
                if s[j] in current_s:
                    break
                current_s.add(s[j])
            best = max(best, len(current_s))
        return best

        
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        best = 0
        for i in range(len(s)):
            count = {}
            max_count = 0
            for j in range(i, len(s)):
                count[s[j]] = count.get(s[j],0)+1
                max_count = max(max_count,count[s[j]])
                if (j-i+1)-max_count<=k:
                    best = max(best, j-i+1)
        return best
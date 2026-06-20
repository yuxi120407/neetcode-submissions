class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l =0
        count = {}
        max_count = 0
        best = 0
        for r in range(len(s)):
            count[s[r]] = 1+ count.get(s[r],0)
            max_count = max(max_count, count[s[r]])

            while (r-l+1)-max_count>k:
                count[s[l]]-=1
                l+=1
            best = max(best, r-l+1)
        return best



        
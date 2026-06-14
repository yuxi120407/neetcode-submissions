from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        else:
            freq_s = Counter(s)
            freq_t = Counter(t)

            for num_s in s:
                if freq_s[num_s]!=freq_t[num_s]:
                    return False


        return True

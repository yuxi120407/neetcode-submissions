from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        for i in range(len(s2)):
            current_str = s2[i:i+len(s1)]
            if Counter(current_str)==Counter(s1):
                return True
        return False
        
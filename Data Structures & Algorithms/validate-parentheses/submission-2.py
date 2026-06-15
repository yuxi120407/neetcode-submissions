class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closehash = {")":"(","]":"[","}":"{"}
        for c in s:
            if c in closehash:
                if stack and stack[-1]==closehash[c]:
                    stack.pop()
                else:
                    return False
            else:
            
                stack.append(c)
        
        if stack:
            return False
        else:
            return True





        
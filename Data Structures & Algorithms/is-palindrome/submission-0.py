class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = ""
        for string in s:
            if string.isalnum():
                new_s+=string.lower()
        print(new_s)
        return new_s == new_s[::-1]

        
        
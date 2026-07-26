class Solution:
    def isPalindrome(self, s: str) -> bool:
        pa_s = ''
        for char in s.lower():
            if char.isalnum():
                pa_s += char
    
        if pa_s[::-1] == pa_s:
            return True
        else:
            return False
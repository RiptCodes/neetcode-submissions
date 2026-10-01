class Solution:
    def isPalindrome(self, s: str) -> bool:
        # reversed_s = s[::-1]
        # for c in s:
        cleaned = ""

        for character in s:
            if character.isalnum():
                cleaned += character.lower()
        
        reverse = "".join(reversed(cleaned))
        return cleaned == reverse

            
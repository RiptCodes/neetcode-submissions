class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {'[': ']', '{': '}', '(': ')'}
        stack = []
        for char in s:
            if char in pairs:                            # it's an OPENER
                stack.append(char)
            else:                                        # it's a CLOSER
                if not stack or pairs[stack.pop()] != char:
                    return False
        return not stack
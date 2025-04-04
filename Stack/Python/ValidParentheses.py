class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = {
            '}': '{',
            ']': '[',
            ')': '('
        }

        stack = []

        for char in s:
            if char in closeToOpen.values():  # char is opening bracket
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                openingBracket = stack.pop()
                if closeToOpen[char] != openingBracket:
                    return False

        if len(stack) != 0:
            return False

        return True

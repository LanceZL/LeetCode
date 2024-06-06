class ValidParentheses:
    """
        Problem:    020. Valid Parentheses
        Link:       https://leetcode.com/problems/valid-parentheses/description/
    """
    # def isValid(self, s: str) -> bool:
    #     # base case
    #     if len(s) <= 1:
    #         return False
        
    #     # Use a stack to track the order, push the corresponding right parentheses into the stack.
    #     stack = []
    #     for p in s:
    #         if p == '(':
    #             stack.append(')')
    #         elif p == '[':
    #             stack.append(']')
    #         elif p == '{':
    #             stack.append('}')
    #         else:  # encounter a reverse parentheses.
    #             # left parenthese must shows before the right one.
    #             if len(stack) == 0 or stack[-1] != p:
    #                 return False
    #             stack.pop()
    #     return len(stack) == 0
    
    def isValid(self, s: str) -> bool:
        """
        Use a mapping to simplify code
        """
        # base case
        if len(s) <= 1:
            return False

        mappings = {'(':')', '[':']', '{':'}'}
        # Use a stack to track the order, push the corresponding right parentheses into the stack.
        stack = []
        for p in s:
            if p in mappings:
                stack.append(mappings[p])
            else:  # encounter a reverse parentheses.
                # left parenthese must shows before the right one.
                if len(stack) == 0 or stack[-1] != p:
                    return False
                stack.pop()
        return len(stack) == 0

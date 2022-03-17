class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        return eval(s.replace(")(", ")+(").replace("()", "1").replace(")", ")*2"))
                
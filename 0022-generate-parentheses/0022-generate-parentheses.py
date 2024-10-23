class Solution:
    def generateParenthesis(self, n):
        result = []
        stack = []

        def dfs(opening, closing):
            if opening == n and closing == n:
                result.append("".join(stack))

            if opening < n:
                stack.append("(")
                dfs(opening+1, closing)
                stack.pop()
            if opening > closing:
                stack.append(")")
                dfs(opening, closing+1)
                stack.pop()

        dfs(0, 0)
        return result
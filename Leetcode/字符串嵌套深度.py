import os

os.system('cls')

class Solution:
    def solve(self, seq):
        ans = []
        depth = 0
        res = 0
        for i in range(len(s)):
            if s[i] == '(':
                depth += 1
                ans.append(depth % 2)
                res = max(res, depth)
            elif s[i] == ')':
                ans.append(depth % 2)
                depth -= 1
        print(ans)
        return res

s = '(()(())())'
sol = Solution()
print(sol.solve(s))
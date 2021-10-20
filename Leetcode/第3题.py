import os

os.system('cls')
s = '10x10x2@3@4@5+1'# 3101
# s = '10+2@1x2'
# 10+2@1x2 16
# 1@2@3 7
# 2@3@4@5 31
# 10+2@3@4@5 41
# 10x10x2@3@4@5+1 3101
# 10@50x2
# 10x10x2@3@4@5+1@2@3x10
pri = {'+':3, 'x':2, '@':1}
class Solution:
    def solve(self, s):
        s = s.strip()
        stack = []
        op = []
        num = 0
        i = 0
        sign = '+'
        signs = set(['x', '@', '-','+'])
        while i < len(s):
            if s[i] not in signs:
                num = num*10 + int(s[i])  
            else:
                stack.append(num)
                num = 0
                if not op:
                    op.append(s[i])
                else:
                    while op and pri[s[i]] >= pri[op[-1]]:
                        num2 = stack.pop()
                        num1 = stack.pop()
                        opt = op.pop()
                        if opt=='@':
                            num3 = num1 | (num1 + num2)
                        if opt == 'x':
                            num3 = num1*num2
                        if opt == '+':
                            num3 = num1 + num2
                        stack.append(num3)
                    op.append(s[i])
            i += 1
        if num != 0:
            stack.append(num)
        print(stack)
        print(op)
        # stack = stack[::-1]
        # op = op[::-1]
        while op:
            opt = op[-1]
            b = stack[-1]
            op.pop()
            stack.pop()
            if opt=='@':
                stack[-1] = stack[-1] | (stack[-1] + b)
            if opt == 'x':
                stack[-1] = stack[-1]*b
            if opt == '+':
                stack[-1] = stack[-1] + b
        return stack[-1]

sol = Solution()
print(sol.solve(s))
        
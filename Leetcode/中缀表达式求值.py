import os
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
# 返回表达式的值
# @param s string字符串 待计算的表达式
# @return int整型
#
os.system('cls')
class Solution:
    def solve(self , s ):
        # write code here
        stack = []
        number = 0
        sign = "+"
        signs = set(['+', '-', '/', '*', '(', ')'])
        i = 0
        while i < len(s):
            c = s[i]
            if c == " ":
                continue
            if ord(c)-ord('0')>=0 and ord(c)-ord('9')<=0:
                number = number*10 + ord(c)-ord('0')
            if c=='(':
                j = i+1
                counterPartition = 1
                while counterPartition > 0 and j<len(s):
                    if s[j] == '(':
                        counterPartition += 1
                    elif s[j] == ')':
                        counterPartition -= 1
                    j += 1
                number = self.solve(s[i+1: j-1])
                print(s[i+1:j-1], s[j-1], number, sign, stack)
                i = j-1
            
            if c in signs or i==len(s)-1:
                if sign == '+':
                    stack.append(number)
                if sign == '-':
                    stack.append(-number)
                if sign =='/':
                    stack.append(int(stack.pop()/number))
                if sign == '*':
                    stack.append(stack.pop()*number)
                sign = c
                number = 0
            i += 1
        ans = sum(stack)
        return ans
    
sol = Solution()
s = "(3+4)*(5+(2-3))"
print(sol.solve(s))


class Solution:
    def solve(self, arr):
        
        num_stack = []
        option_stack = []
        for i in range(len(arr)):
            if arr[i] > '0' and arr[i] <= '9':
                num_stack.append(int(arr[i]))
                continue
            num2 = num_stack.pop()
            num1 = num_stack.pop()
            if arr[i] == '+':
                num_stack.append(num1 + num2)
            if arr[i] == '-':
                num_stack.append(num1 - num2)
            if arr[i] == '*':
                num_stack.append(num1 * num2)
            if arr[i] == '/':
                num_stack.append(num1 // num2)
        return num_stack[-1]

sol = Solution()
arr = ["2","1","+","3","*"]
print(sol.solve(arr))
                
                

                

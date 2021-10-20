import os
os.system('cls')

class Solution:
    def solve(self, s, k):
        return self.dfs(s, 0, len(s)-1, k)
    
    def dfs(self, s, left, right, k):
        total = [0 for _ in range(26)]
        for i in range(left, right+1):
            total[ord(s[i])-ord('a')] += 1
        split = 0
        for i in range(26):
            if total[i]>0 and total[i]<k:
                split = chr(ord('a')+i)
                break
        if split == 0:
            return right-left+1
        i = left
        res = 0
        while i<=right:
            while i<=right and s[i]==split:
                i += 1
            start = i
            if start > right:
                break
            while i<=right and s[i]!=split:
                i+=1
            end = i
            res = max(res, self.dfs(s, start, end-1, k))
        return res


if __name__=="__main__":
    sol = Solution()
    s = 'aaabaabaab'
    print(sol.solve(s,4))
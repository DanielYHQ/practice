
class sss:
    def __init__(self):
        pass
    def tenToN(self, num, N):
        s = "0123456789ABCDEF"
        res = ''
        sign, val = 1, num
        if val < 0:
            sign, val = -1, -val
        while val != 0:
            res += s[int(val%N)]
            val = val // N

        if sign < 0:
            res += '-'
        return res[::-1]

    def nToTen(self, num, N):
        s = str(num)
        sign, val = 1, 0
        for i in range(len(s)):
            if s[i] == '-':
                sign = -1
                continue
            if s[i] == '+':
                continue
            val = val*N + ord(s[i]) - ord('0')

        return val*sign

if __name__ == '__main__':
        sol = sss()
        a = sol.tenToN(100, 2)
        print(a)
        print(sol.nToTen(a, 2))

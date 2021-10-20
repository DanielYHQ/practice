
import math
import os

os.system('cls')
def possion(k, lamb=5):
    possibility = pow(lamb, k)*math.exp(-lamb)
    for i in range(1, k+1):
        possibility /= i
    return possibility

for delta in range(0,100):
    print(round(possion(delta),2), end=' ')
    
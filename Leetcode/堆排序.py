import os
os.system('cls')

def heapsort(arr, l, r):
    tmp = arr[l]
    while 2*l+1 < r:
        child = 2*l + 1
        if child+1 < r and arr[child]>arr[child+1]:
            child += 1
        if arr[child] >= tmp:
            break
        else:
            arr[l] = arr[child]
            l = child
    arr[l] = tmp


arr = [1, 2 ,5, 4, 2 ,1, 9]

for i in reversed(range(len(arr)//2)):
    heapsort(arr, i, len(arr))
print(arr)
for i in reversed(range(len(arr))):
    arr[0], arr[i] = arr[i], arr[0]
    heapsort(arr, 0, i)
print(arr)
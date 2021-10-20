

def quick(arr, l, r):
    if l>=r:
        return
    low, high = l, r
    key = arr[l]
    while low < high:
        while low<high and arr[high]>=key:
            high -= 1
        arr[low] = arr[high]
        while low<high and arr[low]<key:
            low += 1
        arr[high]= arr[low]
    arr[low] = key
    quick(arr, l, low-1)
    quick(arr, low+1, r)

arr = [1, 4,3, 2, 5]
quick(arr, 0, len(arr)-1)
print(arr)
class GuiBing:
    def sort(self, arr):
        tmp = [ 0 for _ in range(len(arr))]
        self.sortarr(arr, tmp, 0, len(arr)-1 )

    def sortarr(self, arr, tmp, l, r):
        if l<r:
            mid = (l+r) // 2
            self.sortarr(arr, tmp, l, mid)
            self.sortarr(arr, tmp, mid+1, r)

            left, right = l, mid+1
            t = l
            while left <= mid and right <= r and t<=r:
                if arr[left] <= arr[right]:
                    tmp[t] = arr[left]
                    left += 1
                else:
                    tmp[t] = arr[right]
                    right+=1
                t += 1

            while left <= mid and t<=r:
                tmp[t] = arr[left]
                left += 1
                t += 1
            while right <= r and t<=r:
                tmp[t] = arr[right]
                right += 1
                t += 1
            for i in range(l, r+1):
                arr[i] = tmp[i]
sol = GuiBing()

arr = [5, 4, 3, 2, 1]

print(sol.sort(arr))
print(arr)
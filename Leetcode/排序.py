


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
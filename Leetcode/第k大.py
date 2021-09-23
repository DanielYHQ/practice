import collections

def quickChoose(arr, k):
    return findK(arr, 0, len(arr)-1, k)

def findK(arr, l, r, k):
    if l <= r:
        pos = kthLargest(arr, l, r, k)
        while pos != k-1:
            if pos > k-1:
                pos = kthLargest(arr, l, pos-1, k)
            else:
                pos = kthLargest(arr, pos+1, r, k)
    return arr[pos]

def kthLargest(arr, le, ri, k):
    key = arr[le]
    l, r = le, ri
    while l<r:
        while l<r and arr[r]<=key:
            r -= 1
        arr[l] = arr[r]
        while l<r and arr[l]>key:
            l+=1
        arr[r] = arr[l]
    arr[l] = key

    return l

class Solution:
    def findKth(self, a, n, K):
        # write code here
        l, r = 0, n-1
        pos = self.partition(a, l, r, K)
        while pos+1 != K:
            if pos+1 > K:
                pos = self.partition(a, l, pos, K)
            else:
                pos = self.partition(a, pos+1, r, K)
        return a[pos]

    def partition(self, a,l, r, K):
        key = a[l]
        left, right = l, r
        while left < right:
            while left < right and a[right]<=key:
                right -= 1
            a[left] = a[right]
            while left < right and a[left] > key:
                left +=1
            a[right] = a[left]
        a[left] = key
        return left

def findK2(arr, start, end, k):
    l, r = start, end
    key = arr[l]
    while l<r:
        while l<r and arr[r]<=key:
            r -= 1
        arr[l] = arr[r]
        while l<r and arr[l] >key:
            l += 1
        arr[r] = arr[l]
    if l == k-1:
        return arr[l]
    elif l>k-1:
        return findK2(arr, start, l-1, k)
    else:
        return findK2(arr, l+1, end, k)
if __name__ == "__main__":
    arr = [1,4,5,6, 7, 9]
    k = 4
    print(quickChoose(arr, k))
    sol = Solution()
    print(sol.findKth(arr, len(arr), k))
    print(findK2(arr, 0, len(arr)-1, k))
